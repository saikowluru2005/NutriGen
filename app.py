# from flask import Flask, render_template, request, redirect, url_for, make_response
# from flask_sqlalchemy import SQLAlchemy
# import os
# from dotenv import load_dotenv
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# load_dotenv(dotenv_path="D:/Python/Nascom/.env")

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# class User(UserMixin,db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
# @app.before_request
# def no_cache():
#     if request.endpoint not in ['static']:
#         response = make_response()
#         response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#         response.headers['Pragma'] = 'no-cache'
#         response.headers['Expires'] = '0'

# @app.before_request
# def require_login():
#     if request.endpoint in ['dashboard', 'macro_micro', 'letsmakerecipe', 'chatwithus', 'custommeal'] and not current_user.is_authenticated:
#         return redirect(url_for('login'))
# @app.route('/', methods=['GET', 'POST'])
# def ope():
#     return render_template('index.html')

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         if not username or not password:
# #             return render_template('login.html')
# #         user = User.query.filter_by(username=username).first()
# #         if user and check_password_hash(user.password, password):
# #             # flash('Logged in successfully.', 'success')
# #             return redirect(url_for('dashboard',username=username))
# #         else:
# #             return render_template('login.html',error='Invalid username and password')
# #     return render_template('login.html')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('dashboard'))
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if not username or not password:
#             # flash('Please enter username and password.', 'error')
#             return render_template('login.html')
#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             login_user(user) 
#             return redirect(url_for('dashboard')) 
#         else:
#             # flash('Invalid username and password.', 'error')
#             return "Invalid Login and password"
#     # return render_template('login.html')
#     response = make_response(render_template('login.html'))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response
# @app.route('/index',methods=['GET','POST'])
# # def index():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         hashed_password = generate_password_hash(password)
# #         new_user = User(username=username, password=hashed_password)
# #         db.session.add(new_user)
# #         db.session.commit()
# #         return redirect(url_for('login')) 
# #     return render_template('signup.html')
# def index():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if not username or not password:
#             return render_template('signup.html', error="All fields are required")

#         hashed_password = generate_password_hash(password)
#         new_user = User(username=username, password=hashed_password)
#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect(url_for('login'))
#         except:
#             return render_template('signup.html', error="Username already exists")
    
#     return render_template('signup.html')
# # @app.route('/dashboard/<username>')
# # def dashboard(username):
# #     user=User.query.filter_by(username=username).first()
# #     if user:
# #         return render_template('dashboard.html',username=username)
# #     else:
# #         return redirect(url_for('login'))
# @app.route('/dashboard') 
# @login_required 
# def dashboard():
#     response = make_response(render_template('dashboard.html', username=current_user.username))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

# # @app.route('/logout')
# # @login_required
# # def logout():
# #     logout_user()
# #     response = make_response(redirect(url_for('login')))
# #     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
# #     response.headers['Pragma'] = 'no-cache'
# #     response.headers['Expires'] = '0'
# #     return response
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     response = make_response(redirect(url_for('login')))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

# # @app.route('/dashboard/<username>/marco_micro')
# # def marco_micro(username):
# #     return render_template('mm.html',username=username)
# # @app.route('/dashboard/<username>/marco_micro')
# # @login_required
# # def marco_micro(username):
# #     return render_template('mm.html', username=username)
# @app.route('/macro_micro')
# @login_required
# def macro_micro():
#     return render_template('mm.html', username=current_user.username)

# @app.route('/letsmakerecipe')
# @login_required
# def letsmakerecipe():
#     return render_template('lmr.html', username=current_user.username)

# @app.route('/chatwithus')
# @login_required
# def chatwithus():
#     return render_template('chat.html', username=current_user.username)

# @app.route('/custommeal')
# @login_required
# def custommeal():
#     return render_template('cmp.html', username=current_user.username)

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
# from flask_sqlalchemy import SQLAlchemy
# import os
# from dotenv import load_dotenv
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# import google.generativeai as ai

# load_dotenv(dotenv_path="C:/Users/saiko/Music/NutriGen/.env")
# # load_dotenv(dotenv_path="C:\\Users\\saiko\\Music\\NutriGen\\.env")

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
# apikey=os.getenv("API_KEY")
# ai.configure(api_key=apikey)
# model = ai.GenerativeModel("gemini-2.0-flash")

# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     name = db.Column(db.String(120), nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# @app.before_request
# def no_cache():
#     if request.endpoint not in ['static']:
#         response = make_response()
#         response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#         response.headers['Pragma'] = 'no-cache'
#         response.headers['Expires'] = '0'

# @app.before_request
# def require_login():
#     if request.endpoint in ['dashboard', 'macro_micro', 'letsmakerecipe', 'chatwithus', 'custommeal'] and not current_user.is_authenticated:
#         return redirect(url_for('login'))

# @app.route('/', methods=['GET', 'POST'])
# def ope():
#     return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('dashboard'))
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if not username or not password:
#             return render_template('login.html')
#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             login_user(user)
#             return redirect(url_for('dashboard'))
#         else:
#             return "Invalid password and username"
#     response = make_response(render_template('login.html'))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         name=request.form['name']
#         if not username or not password:
#             return render_template('signup.html', error="All fields are required")

#         hashed_password = generate_password_hash(password)
#         new_user = User(username=username, password=hashed_password,name=name)
#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect(url_for('login'))
#         except:
#             return render_template('signup.html', error="Username already exists")

#     response = make_response(render_template('signup.html'))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     user = User.query.get(current_user.id)
#     response = make_response(render_template('dashboard.html', username=current_user.username,name=user.name))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     response = make_response(redirect(url_for('logoutpage')))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response
# @app.route('/logoutpage',methods=['GET','POST'])
# def logoutpage():
#     return render_template('index.html')
# # @app.route('/macro_micro')
# # @login_required
# # def macro_micro():
# #     response = ""
# #     if request.method == "POST":
# #         ask = request.form.get("ask")
# #         prompt = f"Give me the macros and it's propotion, micros and it's propotion, and calorie content in {ask} in 100 words, give output without bolding of any word in point-wise format. Provide separate sections for micros and macros.\n\n"
        
# #         try:
# #             result = model.generate_content(prompt)
# #             response = result.text if result.text else "No response from the model."
# #         except Exception as e:
# #             response = f"Error: {e}"
# #     response = make_response(render_template('mm.html', username=current_user.username,response=response))
# #     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
# #     response.headers['Pragma'] = 'no-cache'
# #     response.headers['Expires'] = '0'
# #     return response

# @app.route('/macro_micro', methods=['GET', 'POST'])
# @login_required
# def macro_micro():
#     user = User.query.get(current_user.id)
#     response = ""
#     if request.method == "POST":
#         ask = request.form.get("ask")
#         prompt = f"Give me the macros and it's propotion, micros and it's propotion, and calorie content in {ask} in 100 words, give output without bolding of any word in point-wise format. Provide separate sections for micros and macros.\n\n"
        
#         try:
#             result = model.generate_content(prompt)
#             response = result.text if result.text else "No response from the model."
#         except Exception as e:
#             response = f"Error: {e}"
#     response = make_response(render_template('mm.html', username=current_user.username, response=response,name=user.name))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

# @app.route('/letsmakerecipe',methods=['GET','POST'])
# @login_required
# def letsmakerecipe():
#     user = User.query.get(current_user.id)
#     response = ""
#     if request.method == "POST":
#         ask = request.form.get("ask")
#         prompt = f"Give me the micros and macros and calorie content in {ask} recipie in 100 words, give output without bolding of any word and give evrything in point-wise format in cluding recipie. Provide separate sections for micros and macros.\n\n"
#         try:
#             result = model.generate_content(prompt)
#             response = result.text if result.text else "No response from the model."
#         except Exception as e:
#             response = f"Error: {e}"
#     response = make_response(render_template('lmr.html', username=current_user.username,response=response,name=user.name))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

# @app.route('/chatwithus')
# @login_required
# def chatwithus():
#     user = User.query.get(current_user.id)
#     response = make_response(render_template('chat.html', username=current_user.username,name=user.name))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response
# @app.route('/ask', methods=['POST'])
# def ask():
#     user_input = request.json.get('message')

#     try:
#         response = model.generate_content(user_input)
#         reply = response.text
#     except Exception as e:
#         reply = f"Error: {str(e)}"
    
#     return jsonify({"reply": reply})

# @app.route('/custommeal',methods=['GET','POST'])
# @login_required
# def custommeal():
#     user = User.query.get(current_user.id)
#     response = ""
#     if request.method == "POST":
#         age= request.form.get("age")
#         height = request.form.get("height")
#         weight = request.form.get("weight")
#         target_weight = request.form.get("target_weight")
#         diet = request.form.get("diet")
#         preferred_vegetables = request.form.get("preferred_vegetables", "No preference")
#         carbs = request.form.get("carbs", "No preference")
#         proteins = request.form.get("proteins", "No preference")
#         fats = request.form.get("fats", "No preference")
#         vitamins = request.form.get("vitamins", "No preference")
#         minerals = request.form.get("minerals", "No preference")
#         allergies = request.form.get("allergies", "No")
#         activity_level = request.form.get("activity_level")
#         notes = request.form.get("notes", "")

#         prompt = f"""
#         Create a personalized meal plan , a {age}-year-old person with a height of {height} cm and a weight of {weight} kg. 
#         Goal is to reach {target_weight} kg.
        
#         Diet preference: {diet}
#         Preferred vegetables: {preferred_vegetables}
#         Macronutrient preferences:
#         - Carbohydrates: {carbs}
#         - Proteins: {proteins}
#         - Fats: {fats}
#         Micronutrient preferences:
#         - Vitamins: {vitamins}
#         - Minerals: {minerals}
#         Allergies: {allergies}
#         Activity level: {activity_level}
        
#         Additional notes: {notes}

#         Provide a detailed 1 week meal plan seperated by each day in 200 words with recipies, in point-wise format, including meals for breakfast, lunch, and dinner.
#         Don;t bold any word
#         """

#         try:
#             result = model.generate_content(prompt)
#             response = result.text if result.text else "No response from the model."
#         except Exception as e:
#             response = f"Error: {e}"

#     response = make_response(render_template('cmp.html', username=current_user.username,response=response,name=user.name))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response


# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import google.generativeai as ai

load_dotenv(dotenv_path="D:/Python/Nascom/.env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
apikey=os.getenv("API_KEY")
ai.configure(api_key=apikey)
model = ai.GenerativeModel("gemini-2.0-flash")

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def no_cache():
    if request.endpoint not in ['static']:
        response = make_response()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'

@app.before_request
def require_login():
    if request.endpoint in ['dashboard', 'macro_micro', 'letsmakerecipe', 'chatwithus', 'custommeal'] and not current_user.is_authenticated:
        return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def ope():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            return render_template('login.html')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "Invalid password and username"
    response = make_response(render_template('login.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name=request.form['name']
        if not username or not password:
            return render_template('signup.html', error="All fields are required")

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password,name=name)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('signup.html', error="Username already exists")

    response = make_response(render_template('signup.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(current_user.id) 
    response = make_response(render_template('dashboard.html', username=current_user.username,name=user.name))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/logout')
@login_required
def logout():
    logout_user()
    response = make_response(redirect(url_for('logoutpage')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
@app.route('/logoutpage',methods=['GET','POST'])
def logoutpage():
    return render_template('logout.html')
# @app.route('/macro_micro')
# @login_required
# def macro_micro():
#     response = ""
#     if request.method == "POST":
#         ask = request.form.get("ask")
#         prompt = f"Give me the macros and it's propotion, micros and it's propotion, and calorie content in {ask} in 100 words, give output without bolding of any word in point-wise format. Provide separate sections for micros and macros.\n\n"
        
#         try:
#             result = model.generate_content(prompt)
#             response = result.text if result.text else "No response from the model."
#         except Exception as e:
#             response = f"Error: {e}"
#     response = make_response(render_template('mm.html', username=current_user.username,response=response))
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response

@app.route('/macro_micro', methods=['GET', 'POST'])
@login_required
def macro_micro():
    user = User.query.get(current_user.id)
    response = ""
    if request.method == "POST":
        ask = request.form.get("ask")
        prompt = f"Give me the macros and it's propotion, micros and it's propotion, and calorie content in {ask} in 100 words, give output without bolding of any word in point-wise format. Provide separate sections for micros and macros.\n\n"
        
        try:
            result = model.generate_content(prompt)
            response = result.text if result.text else "No response from the model."
        except Exception as e:
            response = f"Error: {e}"
    response = make_response(render_template('mm.html', username=current_user.username,name=user.name, response=response))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/letsmakerecipe',methods=['GET','POST'])
@login_required
def letsmakerecipe():
    user = User.query.get(current_user.id)
    response = ""
    if request.method == "POST":
        ask = request.form.get("ask")
        prompt = f"Give me the micros and macros and calorie content in {ask} recipie in 100 words, give output without bolding of any word and give evrything in point-wise format in cluding recipie. Provide separate sections for micros and macros.\n\n"
        try:
            result = model.generate_content(prompt)
            response = result.text if result.text else "No response from the model."
        except Exception as e:
            response = f"Error: {e}"
    response = make_response(render_template('lmr.html', username=current_user.username,name=user.name,response=response))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/chatwithus')
@login_required
def chatwithus():
    user = User.query.get(current_user.id)
    response = make_response(render_template('chat.html', username=current_user.username,name=user.name))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')

    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = f"Error: {str(e)}"
    
    return jsonify({"reply": reply})

@app.route('/custommeal',methods=['GET','POST'])
@login_required
def custommeal():
    user = User.query.get(current_user.id)
    response = ""
    if request.method == "POST":
        age= request.form.get("age")
        height = request.form.get("height")
        weight = request.form.get("weight")
        target_weight = request.form.get("target_weight")
        diet = request.form.get("diet")
        preferred_vegetables = request.form.get("preferred_vegetables", "No preference")
        carbs = request.form.get("carbs", "No preference")
        proteins = request.form.get("proteins", "No preference")
        fats = request.form.get("fats", "No preference")
        vitamins = request.form.get("vitamins", "No preference")
        minerals = request.form.get("minerals", "No preference")
        allergies = request.form.get("allergies", "No")
        activity_level = request.form.get("activity_level")
        notes = request.form.get("notes", "")

        prompt = f"""
        Create a personalized meal plan , a {age}-year-old person with a height of {height} cm and a weight of {weight} kg. 
        Goal is to reach {target_weight} kg.
        
        Diet preference: {diet}
        Preferred vegetables: {preferred_vegetables}
        Macronutrient preferences:
        - Carbohydrates: {carbs}
        - Proteins: {proteins}
        - Fats: {fats}
        Micronutrient preferences:
        - Vitamins: {vitamins}
        - Minerals: {minerals}
        Allergies: {allergies}
        Activity level: {activity_level}
        
        Additional notes: {notes}

        Provide a detailed 1 week meal plan seperated by each day in 200 words with recipies, in point-wise format, including meals for breakfast, lunch, and dinner.
        Don;t bold any word
        """

        try:
            result = model.generate_content(prompt)
            response = result.text if result.text else "No response from the model."
        except Exception as e:
            response = f"Error: {e}"

    response = make_response(render_template('cmp.html', username=current_user.username,name=user.name,response=response))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)