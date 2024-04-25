from app import db, ma

class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Task title: {self.title}, description: {self.description}'

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tasks
        load_instance = True
        sqla_session = db.session

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)