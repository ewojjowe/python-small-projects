import qrcode

from config import SAMPLE_TEXT_TO_GENERATE_QR_CODE

def generate_qr_code(code):
    print(f'Generating QR Code Image for: {code}...')
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("assets/qrimage.png")
    print('Done genrating QR Code image!')

if __name__ == "__main__":
    generate_qr_code(SAMPLE_TEXT_TO_GENERATE_QR_CODE)
