# archivo: cargas_masivas/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import LoteConsultaMasiva

@receiver(post_save, sender=LoteConsultaMasiva)
def notificar_cambio_lote(sender, instance, created, **kwargs):
    if created:
        # Notificar al ADMIN que hay un nuevo lote
        subject = f'Nueva Solicitud de Carga Masiva - {instance.empresa.nombre}'
        message = f'''
        El usuario {instance.usuario_solicitante.username} de la empresa {instance.empresa.nombre}
        ha subido un nuevo lote para procesar.

        Puedes gestionarlo en el panel de administración.
        '''
        # Asegúrate de haber definido ADMIN_EMAIL en settings.py
        send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.ADMIN_EMAIL])
        print(f"Correo de notificación enviado al admin por lote {instance.id}")

    elif instance.estado == 'PROCESADO' and instance.archivo_resultado:
        # Notificar al USUARIO que su lote está listo
        subject = 'Tu Reporte de Consulta Masiva está Listo'
        message = f'''
        Hola {instance.usuario_solicitante.username},

        Tu solicitud de consulta masiva (ID: {instance.id}) ha sido procesada.
        Ya puedes descargar el reporte en PDF desde la sección "Cargas Masivas" de la plataforma.
        '''
        send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.usuario_solicitante.email])
        print(f"Correo de notificación enviado al usuario {instance.usuario_solicitante.email}")