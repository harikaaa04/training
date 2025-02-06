import pandas as pd


def fill_file(name, age, city):
	with open("data.csv", "a") as file:
		file.write(f"\n{name},{age},{city}")

def to_df():
	df = pd.read_csv("data.csv")
	print(df.head())

def main():
	print("Enter Name, Age, City (enter 'exit' to exit)")
	with open("data.csv", "w") as f:
		f.write("Name,Age,City")
	while True:
		inp = input("Enter: ")
		if inp == 'exit':
			break 
		name, age, city = inp.split()	
		fill_file(name, age, city)
	to_df()
	
	
main()