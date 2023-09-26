from flask import Blueprint, render_template, request, flash, redirect, url_for
from .sendmail import send_mail

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        sender = request.form.get("sender")
        senderpassword = request.form.get("senderpassword")
        receiver = request.form.get("receiver")
        emailsubject = request.form.get("emailsubject")
        emailbody = request.form.get("emailbody")
        print(f"Sender: {sender}, Password: {senderpassword}, Receiver: {receiver}, Subject: {emailsubject}, Body: {emailbody}, Password: {senderpassword}")
        if sender and senderpassword and receiver and emailsubject and emailbody:
            send_mail(email_sender=sender, email_password=senderpassword, email_receiver=receiver, subject=emailsubject, body=emailbody)
            flash("Success!")
            return render_template("index.html")
    return render_template("index.html")