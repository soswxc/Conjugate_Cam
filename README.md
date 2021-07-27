# Conjugate_Cam
Python program with GUI for designing Conjugate Cams

This python program is for calculating conjugate cams profile.
The output of the program is 2 dxf files (one for the original cam and one for the conjugate) that
  can directly be used in Autocad or Solidwork or other engineering softwares.
  
** before running the code make sure you have installed the requirements.


Inputs of the program:
	arm length of the follower,
	distance from cam to follower pivot point,
	base circle radius of the cam,
	and radius of the roller follower,
and information about cam motion:
	n is the number of cam motion courses,
	for each course add:
		angle of cam at the end of course,
		angle of the follower at the end of course,
		and motion type,

it is obvious that the angle of cam at the end of the course is equal to the angle of cam at the first of the next course, so it's enough to add only the angle at the end. (angle of cam at the start the first course is 0 and at the end of the last course is 360)    

this program only supports cycloid motion for cam, for cycloid rise use 1, for dwell motion use 2, and for cycloid fall use 3 in motion type box for each course.

Relations and formulas used in this code are based on an article from Wen-Tung Chang & Long-Iong Wu: Calculating conjugate cam profiles by vector equations
https://link.springer.com/article/10.1007/s12206-011-0928-4
