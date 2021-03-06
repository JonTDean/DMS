from src.sorters import third_Sort
from tests.utils import shuffle_Clean_List

assert_Against = [
	"Smith Steve Male 3/3/1985 Red",
	"Seles Monica Female 12/2/1973 Black",
	"Kournikova Anna Female 6/3/1975 Red",
	"Kelly Sue Female 7/12/1959 Pink",
	"Hingis Martina Female 4/2/1979 Green",
	"Bouillon Francis Male 6/3/1975 Blue",
	"Bonk Radek Male 6/3/1975 Green",
	"Bishop Timothy Male 4/23/1967 Yellow",
	"Abercrombie Neil Male 2/13/1943 Tan",
];

def test_third_Sort():
	assert third_Sort(shuffle_Clean_List()) == assert_Against;