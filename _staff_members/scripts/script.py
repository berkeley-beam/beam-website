data = [['Briana Ong', 'IB  2020', 'President', 'briana'],
['Patrick Oare', 'Physics & Math 2019', 'President', 'patricko'],
['Nandika Donthi', 'CS 2019', 'External Affairs Executive', 'nandika'],
['Ashlee Garcia', 'EECS 2019', 'Logistics Executive', 'ashlee'],
['Alison Mathews', 'CivE 2019', 'Site Leading Executive', 'alison'],
['Jocelyn Liu', 'MCB 2020', 'Site Leading Executive', 'jocelyn'],
['Radu Firtat', 'MCB 2020', 'Outreach Executive', 'radu'],
['Rohan Chakraborty', 'ChemE 2019', 'Mentor Dev Executive', 'rohan'],
['Stephanie Huang', 'MCB 2020', 'Curriculum Executive',
'stephanieh'],
['Alex Krentsel', 'EECS & Music 2019', 'External Affairs', 'alex'],
['Alexander Orimoloye', 'BioE 2019', 'Outreach, Site Leading',
'alexander'],
['Claudia Lambert', 'Chemical Biology  2019',
'Mentor Dev, Site Leading', 'claudia'],
['Henry Dong', 'CogSci & MCB 2019', 'Mentor Dev, External Affairs', 
'henry'],
['Jeb Boodry', 'ChemE 2020', 'Curriculum', 'jeb'],
['Mai Nojima', 'MCB & Public Health  2019', 'Logistics, Outreach ',
'mai'],
['Miranda Jen', 'Energy Engineering 2019',
'Mentor Dev, Site Leading', 'miranda'],
['Rachel Jang', 'ChemE 2019', 'Curriculum, Site Leading', 'rachel'],
['Abby Cheng', 'ChemE 2021', 'Logistics, Site Leading', 'abby'],
['Alice Chin', 'CS 2019', 'External Affairs, Site Leading', 'alice'],
['Avani Kelekar', 'MCB-Neuro 2020', 'Mentor Dev', 'avani'],
['Brendan Tsuda', 'Chemical Biology 2021', 'Outreach, Site Leading', 'brendan'],
['Chelsea Yang', 'Chem 2020', 'Curriculum, Logistics', 'chelsea'],
['Darren Kim', 'Econ 2021', 'External Affairs, Site Leading', 'darren'],
['David Paner', 'CS 2021', 'Curriculum, Site Leading', 'david'],
['Erica Liu', 'Chem 2019', 'Curriculum, Outreach', 'erica'],
['Joshua Huang', 'MSE 2019', 'Mentor Dev, Logistics', 'joshua'],
['Kaushal Partani', 'CS 2021', 'External Affairs, Site Leading', 'kaushal'],
['Kelly Chang', 'MCB 2020', 'External Affairs, Outreach', 'kelly'],
['Kelvin Zhang', 'CS 2020', 'External Affairs, Logistics', 'kelvin'],
['Monica Oh', 'IB 2020', 'Curriculum, Outreach', 'monica'],
['Nichole Sun', 'Data Science 2021', 'External Affairs, Mentor Dev', 'nichole'],
['Nico Carballal', 'MechE 2021', 'Curriculum, Outreach', 'nico'],
['Nicole Denamur', 'IB 2020', 'Curriculum, External Affairs', 'nikki'],
['Ningxin Zheng', 'MCB 2021', 'Curriculum, Logistics', 'ningxin'],
['Sophie Yu', 'MCB 2021', 'Curriculum, Site Leading', 'sophie'],
['Stephanie Zhang', 'MCB 2020', 'Curriculum, Logistics', 'stephaniez'],
['Tiffany Tran', 'IB & Psych 2020', 'Mentor Dev, Site Leading', 'tiffany']]

for each in data:
	full_name = each[0]
	major = each[1]
	committees = each[2]
	img = each[3]
	f= open(img+".md","w+")
	f.write("---\n")
	f.write("name: " + full_name + "\n")
	f.write("major: " + major + "\n")
	f.write("position: " + committees + "\n")
	f.write("image_path: " + "https://github.com/berkeley-beam/berkeley-beam.github.io/raw/master/images/2018_2019staff/" + img + ".jpg" + "\n")
	f.write("---")
	f.close()
