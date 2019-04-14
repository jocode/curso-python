# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect
from ContactModel import ContactModel
app = Flask(__name__)
app.secret_key = "some_secret"
app.debug = True

@app.route(r'/', methods=['GET'])
def contact_book():
    contacts = ContactModel.query().fetch()
    return render_template('contact_book.html', contacts=contacts)

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():

    if request.form:
        contact = ContactModel(
            name = request.form.get('name'),
            phone = request.form.get('phone'),
            email=request.form.get('email')
        )

        # Se guarda en la base de datos
        contact.put()
        flash("¡Se añadió el contacto!")

    return render_template('add_contact.html')

@app.route(r'/contacts/<uid>', methods=['GET'])
def contact_detail(uid):
    contact = ContactModel.get_by_id(int(uid))
    return render_template('contact.html', contact=contact)

@app.route(r'/delete', methods=['POST'])
def delete_contact():
    contact = ContactModel.get_by_id(int(request.form.get('uid')))

    if not contact:
        return redirect('/', code=301)

    contact.key.delete()
    return redirect('/')

if __name__ == "__main__":
    app.run()