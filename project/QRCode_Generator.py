import qrcode                #inporting qrcode module

def generate_qrcode (text) :          #defines the function
    
    features = qrcode.QRCode(            #entering the size version we required
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 3,
    )
    
    features.add_data (text)             
    features.make (fit = True)
    img = features.make_image (fill_color = "white", back_color = "black")
    img.save ("QRCODE.png")        #to save qr image
    
generate_qrcode("https://www.instagram.com/adii.10__/") 