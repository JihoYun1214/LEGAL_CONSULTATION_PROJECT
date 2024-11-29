from flask import Flask, render_template, request, jsonify
import os
from PIL import Image
import io
from werkzeug.utils import secure_filename
from cases import CASES, default_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

def analyze_detail(case_type, description):
    sub_types = CASES[case_type]["sub_types"]
    best_sub_type = None
    max_matches = 0
    
    for sub_type, data in sub_types.items():
        matches = sum(1 for keyword in data["keywords"] if keyword in description)
        if matches > max_matches:
            max_matches = matches
            best_sub_type = sub_type
            
    if best_sub_type:
        return sub_types[best_sub_type]["templates"][0]
    return default_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        description = request.form.get('description', '')
        
        case_type = None
        max_matches = 0
        
        for case, data in CASES.items():
            matches = sum(1 for keyword in data["keywords"] if keyword in description)
            if matches > max_matches:
                max_matches = matches
                case_type = case
                
        if case_type:
            template = analyze_detail(case_type, description)
            return render_template('index.html', 
                                description=description,
                                analysis=template)
                                
        return render_template('index.html',
                             description=description, 
                             analysis=default_template)
                             
    except Exception as e:
        return render_template('index.html', 
                             error=str(e))

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
