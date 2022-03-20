import sys
sys.path.append("../libraries")
import libEmailSender

subject = "..."
content = "..."
imageAbsPath = f'...'
receiverEmail = "..."
senderEmail = "..."
senderPassword = "..."

message = libEmailSender.setMessage(subject, content, receiverEmail)
# If you don't need to attach an image - skip the step below...
libEmailSender.attachImageToMessage(message, imageAbsPath)
libEmailSender.sendEmail(message, senderEmail, senderPassword)
