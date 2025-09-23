import pytest
from db import SessionLocal, engine
from models import Student, Base


@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()


def test_add_student(db_session):
    student = Student(name="Alice", age=20)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    assert student.id is not None
    assert student.name == "Alice"

    db_session.delete(student)
    db_session.commit()


def test_update_student(db_session):
    student = Student(name="Bob", age=22)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student.name = "Robert"
    db_session.commit()
    db_session.refresh(student)

    assert student.name == "Robert"

    db_session.delete(student)
    db_session.commit()


def test_delete_student(db_session):
    student = Student(name="Charlie", age=25)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student_id = student.id
    db_session.delete(student)
    db_session.commit()

    deleted = db_session.query(Student).filter_by(id=student_id).first()
    assert deleted is None
