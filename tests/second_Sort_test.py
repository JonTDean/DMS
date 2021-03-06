from src.sorters import second_Sort
from tests.utils import shuffle_Clean_List

assert_Against = [
	"Abercrombie Neil Male 2/13/1943 Tan",
	"Kelly Sue Female 7/12/1959 Pink",
	"Bishop Timothy Male 4/23/1967 Yellow",
	"Seles Monica Female 12/2/1973 Black",
	"Bonk Radek Male 6/3/1975 Green",
	"Bouillon Francis Male 6/3/1975 Blue",
	"Kournikova Anna Female 6/3/1975 Red",
	"Hingis Martina Female 4/2/1979 Green",
	"Smith Steve Male 3/3/1985 Red",
];

def test_second_Sort():
	assert second_Sort(shuffle_Clean_List()) == assert_Against;