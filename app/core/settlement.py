from app.models.settlement import VenueSettlement

def record_settlement(db, bottle_id, venue_id, poured_ml, price_per_ml, currency):
    s = VenueSettlement(
        bottle_id=bottle_id,
        venue_id=venue_id,
        poured_ml=poured_ml,
        price_per_ml=price_per_ml,
        currency=currency
    )
    db.add(s)
    db.commit()

def settle_venue(db, venue_id):
    unsettled = db.query(VenueSettlement)\
        .filter_by(venue_id=venue_id, settled=False).all()

    total = sum(s.poured_ml * s.price_per_ml for s in unsettled)

    for s in unsettled:
        s.settled = True

    db.commit()
    return total
