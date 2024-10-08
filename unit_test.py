import unittest
import sqlite3

class TestWeddingDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test database and populate it with test data
        cls.conn = sqlite3.connect(':memory:')  # In-memory database for testing
        cls.cur = cls.conn.cursor()

        # Create tables
        cls.cur.execute('''
        CREATE TABLE Users (
            user_id TEXT PRIMARY KEY,
            user_name TEXT
        )
        ''')
        cls.cur.execute('''
        CREATE TABLE Weddings (
            user_id TEXT PRIMARY KEY,
            wedding_date DATE,
            FOREIGN KEY(user_id) REFERENCES Users(user_id)
        )
        ''')

        # Insert test data into Users table
        test_users = [
            ('1', 'Alice'),
            ('2', 'Bob'),
            ('3', 'Charlie')
        ]
        cls.cur.executemany('INSERT INTO Users (user_id, user_name) VALUES (?, ?)', test_users)

        # Insert test data into Weddings table
        test_weddings = [
            ('1', '2024-06-15'),
            ('2', '2024-06-20'),
            ('3', '2024-10-01')
        ]
        cls.cur.executemany('INSERT INTO Weddings (user_id, wedding_date) VALUES (?, ?)', test_weddings)

        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def test_users_in_june_2024(self):
        self.cur.execute('''
        SELECT user_name FROM Users
        JOIN Weddings ON Users.user_id = Weddings.user_id
        WHERE strftime('%Y', wedding_date) = '2024' AND strftime('%m', wedding_date) = '06'
        ''')
        june_weddings = self.cur.fetchall()
        self.assertEqual(len(june_weddings), 2)  # Should find Alice and Bob
        self.assertIn(('Alice',), june_weddings)
        self.assertIn(('Bob',), june_weddings)

    def test_upcoming_weddings(self):
        today = '2024-06-01'  # Simulate today's date for testing
        self.cur.execute('''
        SELECT user_name FROM Users
        JOIN Weddings ON Users.user_id = Weddings.user_id
        WHERE wedding_date BETWEEN ? AND ?
        ''', (today, '2024-06-15'))  # Check for upcoming weddings within 2 weeks
        upcoming_weddings = self.cur.fetchall()
        self.assertEqual(len(upcoming_weddings), 1)  # Should find only Alice
        self.assertIn(('Alice',), upcoming_weddings)

if __name__ == '__main__':
    unittest.main()
