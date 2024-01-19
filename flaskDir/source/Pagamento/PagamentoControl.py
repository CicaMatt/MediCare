from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required


from flaskDir.source.Pagamento.PagamentoService import PagamentoService

informazionipersonali_blueprint = Blueprint('informazionipersonali', __name__)




@informazionipersonali_blueprint.route('/pagamento', methods=['GET','POST'])
@login_required
def getMetodi():
    """
    Visualizza la lista dei metodi di pagamento associati all'utente corrente.

    Returns:
        render_template: Template HTML con la lista dei metodi di pagamento.
    """
    da_elimare = request.args.get('pan')
    cf= request.args.get('cf')
    if da_elimare is not None:
        PagamentoService.eliminaMetodo(da_elimare,cf)
    return render_template("InformazioniPersonali.html", lista= PagamentoService.getMetodi(current_user.CF).all())



@informazionipersonali_blueprint.route('/addPagamento', methods=['GET','POST'])
@login_required
def addCarta():
    """
    Aggiunge un nuovo metodo di pagamento (carta di credito) associato all'utente corrente.

    Returns:
        redirect: Reindirizza alla pagina dei metodi di pagamento dopo l'aggiunta.
        render_template: Template HTML di errore se si verifica un problema durante l'aggiunta.
    """
    if request.method == 'POST':
        cvv = request.form.get('cvv')
        pan = request.form.get('pan')
        titolare = request.form.get('titolare')
        mese = request.form.get('mese')
        anno = request.form.get('anno')
        cf = request.form.get('cf')
        scadenza = mese+"/"+anno

        try:
            if not cvv.isdigit() or not len(cvv) in {3}:
                return render_template("ErroreCarta.html")
            if not pan.isdigit() or not len(pan) == 16:
                return render_template("ErroreCarta.html")
            if len(cf)>16:
                return render_template("ErroreCarta.html")
            mese_numero = int(mese)
            if not(1 <= mese_numero <= 12):
                return render_template("ErroreCarta.html")
            anno_numero = int(anno)
            if not(2024 <= anno_numero <= 3000):
                return render_template("ErroreCarta.html")
            if not PagamentoService.addCarta(cvv,pan,titolare,scadenza,cf):
                return render_template("CartaDuplicata.html")
            return redirect(url_for('informazionipersonali.getMetodi'))

        except ValueError as e:
            # Se si verifica un errore, restituisci una pagina di errore con il messaggio
            return render_template("ErroreCarta.html")
