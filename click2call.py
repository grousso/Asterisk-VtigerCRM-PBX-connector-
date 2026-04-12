from flask import Flask, request, jsonify
from asterisk.manager import Manager

app = Flask(__name__)

# Asterisk AMI USER
AMI_HOST = '127.0.0.1'
AMI_USER = 'XXX'
AMI_PASS = 'XXX'

mgr = Manager()

def connect_ami():
    try:
        mgr.connect(AMI_HOST, port=5038)
        mgr.login(AMI_USER, AMI_PASS)
        print("[+] Connected to Asterisk AMI")
    except Exception as e:
        print(f"[-] AMI Connection Error: {e}")

@app.route('/makecall', methods=['GET', 'POST']) # Εδώ επιτρέπουμε και τα δύο
def make_call():
    # Διάβασμα των παραμέτρων όπως τις στέλνει ΤΟ ΔΙΚΟ ΣΟΥ Vtiger
    number_to_call = request.args.get('to')   # Αντί για 'number'
    extension = request.args.get('from')      # Αντί για 'extension'
    secret = request.args.get('secret')       # Προαιρετικό: για ασφάλεια
    secret = hash(secret)
    
    print(f"[*] Request received: From {extension} to {number_to_call}")

    if not number_to_call or not extension:
        return jsonify({"success": False, "message": "Missing 'to' or 'from'"}), 400

    try:
        display_name = f"Vtiger: {number_to_call}"
        mgr.originate(
            channel=f"PJSIP/{extension}", 
            exten=number_to_call,
            context='from-internal',
            priority='1',
            caller_id=display_name # <--- ΑΥΤΟ ΑΛΛΑΖΕΙ ΤΟ CALLER ID
        )
        return jsonify({"success": True, "message": "Call initiated"}), 200
    except Exception as e:
        print(f"[-] Originate Error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    connect_ami()
    # Τρέχουμε στην 5000 (ή όποια πόρτα έχεις δηλώσει στο Vtiger)
    app.run(host='0.0.0.0', port=5000)
