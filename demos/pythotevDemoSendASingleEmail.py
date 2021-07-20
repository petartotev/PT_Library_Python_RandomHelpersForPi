from ..libraries import libEmailSender

subject = "This is a subject123."
content = "This is the content of the email itself."
imagePath = f'...'
receiverEmail = "..."
senderEmail = "..."
senderPassword = "..."

message = libEmailSender.setMessage(subject, content, receiverEmail)
# If you don't need to attach an image - skip the step below...
libEmailSender.attachImageToMessage(message, imagePath)
libEmailSender.sendEmail(message, senderEmail, senderPassword)