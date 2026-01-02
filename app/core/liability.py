from app.models.liability import LiabilityEvent

def record_liability(db, venue_id, transaction_id):
    event = LiabilityEvent(
        venue_id=venue_id,
        transaction_id=transaction_id
    )
    db.add(event)
    db.commit()
