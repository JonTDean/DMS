from src.sorters import first_Sort
from tests.utils import shuffle_Clean_List


assert_Against = [
	"Hingis Martina Female 4/2/1979 Green",
	"Kelly Sue Female 7/12/1959 Pink",
	"Kournikova Anna Female 6/3/1975 Red",
	"Seles Monica Female 12/2/1973 Black",
	"Abercrombie Neil Male 2/13/1943 Tan",
	"Bishop Timothy Male 4/23/1967 Yellow",
	"Bonk Radek Male 6/3/1975 Green",
	"Bouillon Francis Male 6/3/1975 Blue",
	"Smith Steve Male 3/3/1985 Red",
]

def test_First_Sort():
	assert first_Sort(shuffle_Clean_List()) == assert_Against;