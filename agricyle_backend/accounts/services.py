import resend
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_reset_password_email(email, reset_token, frontend_url=None):
    """
    Envoie un email de réinitialisation de mot de passe via Resend
    """
    if not frontend_url:
        frontend_url = "http://localhost:5173"  # URL de votre frontend
    
    reset_link = f"{frontend_url}/reset-password?token={reset_token}&email={email}"
    
    # Préparer le contenu HTML
    html_content = render_to_string('emails/reset_password.html', {
        'reset_link': reset_link,
        'email': email,
    })
    
    # Version texte
    text_content = f"""
    Bonjour,
    
    Vous avez demandé à réinitialiser votre mot de passe Agricyle.
    
    Cliquez sur ce lien pour définir un nouveau mot de passe :
    {reset_link}
    
    Ce lien expirera dans 1 heure.
    
    Si vous n'avez pas fait cette demande, ignorez simplement cet email.
    
    Cordialement,
    L'équipe Agricyle
    """
    
    try:
        # Envoyer l'email avec Resend
        params = {
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": [email],
            "subject": "🔐 Réinitialisation de votre mot de passe Agricyle",
            "html": html_content,
            "text": text_content,
        }
        
        response = resend.Emails.send(params)
        print(f"✅ Email envoyé via Resend à {email}: {response['id']}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur Resend: {str(e)}")
        return False


def send_welcome_email(email, username):
    """
    Envoie un email de bienvenue via Resend
    """
    html_content = render_to_string('emails/welcome.html', {
        'username': username,
        'email': email,
    })
    
    text_content = f"""
    Bienvenue sur Agricyle, {username} !
    
    Votre compte a été créé avec succès.
    
    Connectez-vous pour commencer à utiliser nos services.
    
    Cordialement,
    L'équipe Agricyle
    """
    
    try:
        params = {
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": [email],
            "subject": "🎉 Bienvenue sur Agricyle !",
            "html": html_content,
            "text": text_content,
        }
        
        response = resend.Emails.send(params)
        print(f"✅ Email de bienvenue envoyé à {email}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur Resend: {str(e)}")
        return False