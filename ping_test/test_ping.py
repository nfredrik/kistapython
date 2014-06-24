from ping import create_parser, ping
#from unittest import TestCase
import unittest
class CommandLineTestCase(unittest.TestCase):
    """
    Base TestCase class, sets up a CLI parser
    """
    @classmethod
    def setUpClass(cls):
        parser = create_parser()
        cls.parser = parser

class PingTestCase(CommandLineTestCase):
    def test_with_empty_args(self):
        """
        User passes no args, should fail with SystemExit
        """                                    
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_db_servers_ubuntu_ami_in_australia(self):
        """
        Find database servers with the Ubuntu AMI in Australia region
        """
        args = self.parser.parse_args(['database', '-R', 'australia', '-A', 'idbs81839'])
        result = ping(args.tags, args.region, args.ami)
        self.assertIsNotNone(result)
        # Do some othe assertions on the result


if __name__ == '__main__':
    unittest.main()
