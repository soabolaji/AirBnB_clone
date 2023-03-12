#!/usr/bin/python3
"""Defines unittests for models/place.py.
Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(apl))
        self.assertNotIn("city_id", apl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(apl))
        self.assertNotIn("user_id", apl.__dict__)

    def test_name_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(apl))
        self.assertNotIn("name", apl.__dict__)

    def test_description_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(apl))
        self.assertNotIn("desctiption", apl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(apl))
        self.assertNotIn("number_rooms", apl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(apl))
        self.assertNotIn("number_bathrooms", apl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(apl))
        self.assertNotIn("max_guest", apl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(apl))
        self.assertNotIn("price_by_night", apl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(apl))
        self.assertNotIn("latitude", apl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(apl))
        self.assertNotIn("longitude", apl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        apl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(apl))
        self.assertNotIn("amenity_ids", apl.__dict__)

    def test_two_aplaces_unique_ids(self):
        apl1 = Place()
        apl2 = Place()
        self.assertNotEqual(apl1.id, apl2.id)

    def test_two_aplaces_different_created_at(self):
        apl1 = Place()
        sleep(0.05)
        apl2 = Place()
        self.assertLess(apl1.created_at, apl2.created_at)

    def test_two_aplaces_different_updated_at(self):
        apl1 = Place()
        sleep(0.05)
        apl2 = Place()
        self.assertLess(apl1.updated_at, apl2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        apl = Place()
        apl.id = "123456"
        apl.created_at = apl.updated_at = dt
        aplstr = apl.__str__()
        self.assertIn("[Place] (123456)", aplstr)
        self.assertIn("'id': '123456'", aplstr)
        self.assertIn("'created_at': " + dt_repr, aplstr)
        self.assertIn("'updated_at': " + dt_repr, aplstr)

    def test_args_unused(self):
        apl = Place(None)
        self.assertNotIn(None, apl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        apl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(apl.id, "345")
        self.assertEqual(apl.created_at, dt)
        self.assertEqual(apl.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        apl = Place()
        sleep(0.05)
        first_updated_at = apl.updated_at
        apl.save()
        self.assertLess(first_updated_at, apl.updated_at)

    def test_two_saves(self):
        apl = Place()
        sleep(0.05)
        first_updated_at = apl.updated_at
        apl.save()
        second_updated_at = apl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        apl.save()
        self.assertLess(second_updated_at, apl.updated_at)

    def test_save_with_arg(self):
        apl = Place()
        with self.assertRaises(TypeError):
            apl.save(None)

    def test_save_updates_file(self):
        apl = Place()
        apl.save()
        aplid = "Place." + apl.id
        with open("file.json", "r") as f:
            self.assertIn(aplid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        apl = Place()
        self.assertIn("id", apl.to_dict())
        self.assertIn("created_at", apl.to_dict())
        self.assertIn("updated_at", apl.to_dict())
        self.assertIn("__class__", apl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        apl = Place()
        apl.middle_name = "Holberton"
        apl.my_number = 98
        self.assertEqual("Holberton", apl.middle_name)
        self.assertIn("my_number", apl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        apl = Place()
        apl_dict = apl.to_dict()
        self.assertEqual(str, type(apl_dict["id"]))
        self.assertEqual(str, type(apl_dict["created_at"]))
        self.assertEqual(str, type(apl_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        apl = Place()
        apl.id = "123456"
        apl.created_at = apl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(apl.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        apl = Place()
        self.assertNotEqual(apl.to_dict(), apl.__dict__)

    def test_to_dict_with_arg(self):
        apl = Place()
        with self.assertRaises(TypeError):
            apl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
