from backend import db

class CardList(db.Model):

    __tablename__ = 'card_list'

    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String)
    card_color_identity = db.Column(db.String)
    card_colors = db.Column(db.String)
    card_supertype = db.Column(db.String)
    card_type = db.Column(db.String)

    def __repr__(self):
        return repr(f'Card: {self.card_name}')