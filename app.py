from flask import Flask,request,jsonify

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sql2026@localhost/category_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

app.json.sort_keys = False

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    subtitle = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    image = db.Column(db.String(200), unique=True, nullable=False)
    status= db.Column(db.Boolean, default=True)
    delete_status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, default=None, onupdate=db.func.current_timestamp())
    Updated_at = db.Column(db.DateTime, default=None, onupdate=db.func.current_timestamp())
    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'description': self.description,
            'image': self.image,
            'status': self.status,
            'delete_status': self.delete_status,
            'created_at': self.created_at,
            'deleted_at': self.deleted_at,
            'Updated_at': self.Updated_at
        }
    
@app.route('/')
def Home():
    return jsonify ({'create':'/create','get_data':'/fetch_all','get_data_by_id':'/fetch_by_id/id','update':'/update/id', 'delete':'/delete/id'})

@app.route('/create', methods=['POST'])
def create_Category():

    data = request.get_json()

    if isinstance(data, dict):
        data = [data]

    for item in data:
        category = Category(
            title=item.get('title'),
            subtitle=item.get('subtitle'),
            description=item.get('description'),
            image=item.get('image'),
            status=item.get('status'),
            delete_status=item.get('delete_status')
        )

        db.session.add(category)

    db.session.commit()

    return jsonify({"message": "Categories created successfully"})

@app.route('/fetch_all',methods=['GET'])
def Fetch_All_Categories():
    categories = Category.query.all()
    category_list = [category.to_dict() for category in categories]
    return jsonify(category_list)

@app.route('/fetch_by_id/<int:category_id>', methods=['GET'])
def Fetch_Category_By_Id(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    return jsonify(category.to_dict())






@app.route('/update/<int:category_id>', methods=['PUT'])
def Update_Category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404

    data = request.get_json()
    category.title = data.get('title', category.title)
    category.subtitle = data.get('subtitle', category.subtitle)
    category.description = data.get('description', category.description)
    category.image = data.get('image', category.image)
    category.status = data.get('status', category.status)
    category.delete_status = data.get('delete_status', category.delete_status)

    db.session.commit()
    return jsonify({'message': 'Category updated successfully', 'category': category.to_dict()})







@app.route('/delete/<int:category_id>', methods=['PUT'])
def Delete_Category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'})




if __name__ =='__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)