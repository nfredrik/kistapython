
def test_csv_file(File):
    csv = File('test.csv')
    assert csv.contains('Start')
    assert csv.mode == 644
