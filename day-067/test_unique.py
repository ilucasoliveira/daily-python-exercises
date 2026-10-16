from database import SessionLocal, ProcessedOrder

with SessionLocal() as session:
    new_order1 = ProcessedOrder(order_id="aaa-111")
    session.add(new_order1)
    session.commit()
    print("firt order processed")

    new_order2 = ProcessedOrder(order_id="aaa-111")
    session.add(new_order2)
    session.commit()
    print("second order processed")
