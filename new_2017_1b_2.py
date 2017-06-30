def fun(num,color):
	answer1 = ''
	answer = ''
	answer2 = ''
	answer3 = ''
	new_thing =[0,0,0]
	print color

	if color[1] != 0:
		if color [1] == color[4] and color[0] == 0 and color[2] ==0 and color[3] ==0 and color[5] ==0:
			for i in range(color[1]):
				answer = answer + "OB" 
			return answer
		elif color[1]+1 <= color[4]:
			for i in range (color[1]):
				answer1 = answer1 + 'B'
				answer1= answer1 + 'O'
				color[1] = color[1]-1


				color[4] = color[4]-1
			answer1 =  answer1 + 'B'
			color[4] = color[4]
			new_thing[0] = new_thing[0]+1


		else:
			return "IMPOSSIBLE"
	if color[3] != 0:
		if color [3] == color[0] and color[1] ==0 and color[2] ==0 and color[4] ==0 and color[5] ==0:
			for i in range(color[3]):
				answer = answer + "RG" 
			return answer		
		elif color[3]+1 <= color[0]:
			for i in range (color[3]):
				answer2 =  answer2 + 'R'
				answer2 =  answer2 + 'G'
				color[3] = color[3]-1

				
				color[0] = color[0]-1
			answer2 =  answer2 + 'R'
			color[0] = color[0]
			new_thing[1] = new_thing[1]+1

		else:
			return  "IMPOSSIBLE"

	if color[5] != 0:
		if color [5] == color[2] and color[0] ==0 and color[1] ==0 and color[3] ==0 and color[4] ==0:
			for i in range(color[5]):
				answer = answer + "YV" 	
			return answer	
		if color[5]+1<= color[2]:
			for i in range (color[5]):
				answer3 =  answer3 + 'Y'
				answer3 =  answer3 + 'V'
				color[5] = color[5]-1
				
				color[2] = color[2]-1
			answer3 =  answer3 + 'Y'
			color[2] = color[2]
			new_thing[2] = new_thing[2]+1
		else:
			return "IMPOSSIBLE"

	print color
	
	big_value = max(color)

	big_num = color.count(big_value)
	if big_num == 1:
		big_pos = color.index(big_value)

		if big_pos ==0:
			second = color[2]
			third = color[4]
			big = 'R'
			s = 'Y'
			t = 'B'
			O_Z ='YB'
			
		elif big_pos ==2:
			second = color[0]
			third = color[4]
			big = "Y"
			s = 'R'
			t = 'B'
			O_Z ='RB'		
		elif big_pos == 4:
			second = color[0]
			third = color[2]
			s = 'R'
			t = 'Y'
			O_Z ='YR'
			big = 'B'










		# if answer1 != '':
		# 	print color

		# 	if answer1[0] == 'Y':
		# 		space = color[2] +1
		# 		if ( space <= color[0]+color[4] ):
		# 			if color[0] >= color[4] and color[4] *2 >= color[0]:
		# 				if space > color[0]:
		# 					left_1 = space - color[0]
		# 					left_2 = color[4] - left_1
		# 					left_3 = color[0] -left_2
		# 					for i in range (left_2):
		# 						answer1 = answer1 + 'RBY'
		# 					for i in range(left_3):
		# 						answer1 = answer1 + 'RY'
		# 					for i in range(left_1):
		# 						answer1 = answer1 + 'BY'
		# 					return answer1[:-1]
		# 				else:
		# 					big_left = color[0] - space

		# 					if big_left<= color[4]*2:
								
		# 						if color[4] >= space:
		# 							small_left = color[4] - space
		# 							big_left = big_left - small_left
		# 							double = big_left/2
		# 							one = big_left%2
		# 							only = space - double -one
		# 							for i in range (double):
		# 								answer1 = answer1 + 'RBRY'
		# 							for i in range(one):
		# 								answer1 = answer1 + 'RBY'
		# 							for i in range (only-1):
		# 								answer1 = answer1 + 'RY'
		# 							answer1 = answer1 + 'R'
		# 							for i in range (small_left):
		# 								answer1 = answer1 +'BR'


		# 							return answer1



		# 						else:
		# 							double = big_left/2
		# 							one = big_left%2
		# 							only = space - double -one
		# 							for i in range (double):
		# 								answer1 = answer1 + 'RBRY'
		# 							for i in range(one):
		# 								answer1 = answer1 + 'RBY'
		# 							for i in range (only):
		# 								answer1 = answer1 + 'RY'
		# 							return answer1[:-1]
		# 					else:
		# 						return "IMPOSSIBLE"





		# 			elif color[4]>color[0] and color[0] *2 >= color[4]:
		# 				if space >= color[4]:
		# 					left_1 = space - color[4]
		# 					left_2 = color[0] - left_1
		# 					left_3 = color[4] -left_2
		# 					for i in range (left_2):
		# 						answer1 = answer1 + 'RBY'
		# 					for i in range(left_3):
		# 						answer1 = answer1 + 'BY'
		# 					for i in range(left_1):
		# 						answer1 = answer1 + 'RY'
		# 					return answer1[:-1]
		# 				else:

		# 					big_left = color[4] - space

		# 					if big_left<= color[0]*2:
								
		# 						if color[0] >= space:
		# 							small_left = color[0] - space
		# 							big_left = big_left - small_left
		# 							double = big_left/2
		# 							one = big_left%2
		# 							only = space - double -one
		# 							for i in range (double):
		# 								answer1 = answer1 + 'BRBY'
		# 							for i in range(one):
		# 								answer1 = answer1 + 'RBY'
		# 							for i in range (only-1):
		# 								answer1 = answer1 + 'BY'
		# 							answer1 = answer1 + 'B'
		# 							for i in range (small_left):
		# 								answer1 = answer1 +'RB'


		# 							return answer1



		# 						else:
		# 							double = big_left/2
		# 							one = big_left%2
		# 							only = space - double -one
		# 							for i in range (double):
		# 								answer1 = answer1 + 'BRBY'
		# 							for i in range(one):
		# 								answer1 = answer1 + 'RBY'
		# 							for i in range (only):
		# 								answer1 = answer1 + 'BY'
		# 							return answer1[:-1]
		# 					else:
		# 						return "IMPOSSIBLE"

					







			# elif answer1[0] =='B':
			# 	space = color[4] +1
			# 	if ( space <= color[0]+color[2]):
			# 		if color[0] >= color[2] and color[2] *2 >= color[0]:
			# 			if space >= color[0]:
			# 				left_1 = space - color[0]
			# 				left_2 = color[2] - left_1
			# 				left_3 = color[0] -left_2
			# 				for i in range (left_2):
			# 					answer1 = answer1 + 'RYB'
			# 				for i in range(left_3):
			# 					answer1 = answer1 + 'RB'
			# 				for i in range(left_1):
			# 					answer1 = answer1 + 'YB'
			# 				return answer1[:-1]
			# 			else:
			# 				big_left = color[0] - space

			# 				if big_left<= color[2]*2:
								
			# 					if color[2] >= space:
			# 						small_left = color[2] - space
			# 						big_left = big_left - small_left
			# 						double = big_left/2
			# 						one = big_left%2
			# 						only = space - double -one
			# 						for i in range (double):
			# 							answer1 = answer1 + 'RYRB'
			# 						for i in range(one):
			# 							answer1 = answer1 + 'RYB'
			# 						for i in range (only-1):
			# 							answer1 = answer1 + 'RB'
			# 						answer1 = answer1 + 'R'
			# 						for i in range (small_left):
			# 							answer1 = answer1 +'YR'


			# 						return answer1



			# 					else:
			# 						double = big_left/2
			# 						one = big_left%2
			# 						only = space - double -one
			# 						for i in range (double):
			# 							answer1 = answer1 + 'RYRB'
			# 						for i in range(one):
			# 							answer1 = answer1 + 'RYB'
			# 						for i in range (only):
			# 							answer1 = answer1 + 'RB'
			# 						return answer1[:-1]
			# 				else:
			# 					return "IMPOSSIBLE"




			# 		elif color[2]>color[0] and color[0] *2 >= color[2]:
			# 			if space >= color[2]:
			# 				left_1 = space - color[2]
			# 				left_2 = color[0] - left_1
			# 				left_3 = color[2] -left_2
			# 				for i in range (left_2):
			# 					answer1 = answer1 + 'RYB'
			# 				for i in range(left_3):
			# 					answer1 = answer1 + 'YB'
			# 				for i in range(left_1):
			# 					answer1 = answer1 + 'RB'
			# 				return answer1[:-1]
			# 			else:
			# 				big_left = color[2] - space

			# 				if big_left<= color[0]*2:
								
			# 					if color[0] >= space:
			# 						small_left = color[0] - space
			# 						big_left = big_left - small_left
			# 						double = big_left/2
			# 						one = big_left%2
			# 						only = space - double -one
			# 						for i in range (double):
			# 							answer1 = answer1 + 'RYB'
			# 						for i in range(one):
			# 							answer1 = answer1 + 'RYB'
			# 						for i in range (only-1):
			# 							answer1 = answer1 + 'YB'
			# 						answer1 = answer1 + 'Y'
			# 						for i in range (small_left):
			# 							answer1 = answer1 +'RY'


			# 						return answer1



			# 					else:
			# 						double = big_left/2
			# 						one = big_left%2
			# 						only = space - double -one
			# 						for i in range (double):
			# 							answer1 = answer1 + 'YRYB'
			# 						for i in range(one):
			# 							answer1 = answer1 + 'RYB'
			# 						for i in range (only):
			# 							answer1 = answer1 + 'YB'
			# 						return answer1[:-1]
			# 				else:
			# 					return "IMPOSSIBLE"

			# elif answer1[0] =='R':
			# 	space = color[0] +1
			# 	print space
			# 	if ( space <= color[2]+color[4]):
			# 		if color[2] >= color[4] and color[4] *2 >= color[2]:
			# 			if space >= color[2]:
			# 				left_1 = space - color[2]
			# 				left_2 = color[4] - left_1
			# 				left_3 = color[2] -left_2
			# 				for i in range (left_2):
			# 					answer1 = answer1 + 'YBR'
			# 				for i in range(left_3):
			# 					answer1 = answer1 + 'YR'
			# 				for i in range(left_1):
			# 					answer1 = answer1 + 'BR'
			# 				return answer1[:-1]
			# 			else:
			# 				big_left = color[2] - space

			# 				if big_left<= color[4]*2:
								
			# 					if color[4] >= space:
			# 						small_left = color[4] - space
			# 						big_left = big_left - small_left
			# 						double = big_left/2
			# 						one = big_left%2
			# 						only = space - double -one
			# 						for i in range (double):
			# 							answer1 = answer1 + 'YBYR'
			# 						for i in range(one):
			# 							answer1 = answer1 + 'YBR'
			# 						for i in range (only-1):
			# 							answer1 = answer1 + 'YR'
			# 						answer1 = answer1 + 'Y'
			# 						for i in range (small_left):
			# 							answer1 = answer1 +'BY'


			# 						return answer1



			# 					else:
			# 						double = big_left/2
			# 						one = big_left%2
			# 						only = space - double -one
			# 						for i in range (double):
			# 							answer1 = answer1 + 'YBYR'
			# 						for i in range(one):
			# 							answer1 = answer1 + 'BYR'
			# 						for i in range (only):
			# 							answer1 = answer1 + 'YR'
			# 						return answer1[:-1]
			# 				else:
			# 					return "IMPOSSIBLE"



			# 		elif color[4]>color[2] and color[2] *2 >= color[4]:
			# 			if space >= color[4]:
			# 				left_1 = space - color[4]
			# 				left_2 = color[2] - left_1
			# 				left_3 = color[4] -left_2
			# 				for i in range (left_2):
			# 					answer1 = answer1 + 'YBR'
			# 				for i in range(left_3):
			# 					answer1 = answer1 + 'BR'
			# 				for i in range(left_1):
			# 					answer1 = answer1 + 'YR'
			# 				return answer1[:-1]
			# 			else:
			# 				big_left = color[4] - space

			# 				if big_left<= color[2]*2:

								
			# 					if color[2] >= space:
			# 						small_left = color[2] - space
			# 						big_left = big_left - small_left
			# 						double = big_left/2
			# 						one = big_left%2
			# 						only = space - double -one
			# 						for i in range (double):
			# 							answer1 = answer1 + 'BYBR'
			# 						for i in range(one):
			# 							answer1 = answer1 + 'BYR'
			# 						for i in range (only-1):
			# 							answer1 = answer1 + 'BR'
			# 						answer1 = answer1 + 'B'
			# 						for i in range (small_left):
			# 							answer1 = answer1 +'YB'


			# 						return answer1



			# 					else:
			# 						double = big_left/2
			# 						one = big_left%2
			# 						only = space - double -one
			# 						for i in range (double):
			# 							answer1 = answer1 + 'BYBR'
			# 						for i in range(one):
			# 							answer1 = answer1 + 'BYR'
			# 						for i in range (only):
			# 							answer1 = answer1 + 'BR'

			# 						return answer1[:-1]
			# 				else:
			# 					return "IMPOSSIBLE"




			


















		if (second+third) >=big_value:
			if second >= third:
				left_1 = big_value - second
				left_2 = third - left_1
				left_3 = second - left_2  
				for i in range (left_2):
					answer = answer + O_Z + big  
				for i in range (left_3):
					answer = answer + s + big
				for i in range (left_1 ):
					answer = answer + t + big
				if len(answer) != num:
					print len(answer)
					print num
					print False,1
			else:
				left_1 = big_value - third
				left_2 = second - left_1
				left_3 = third - left_2 
				for i in range (left_2):
					answer = answer + O_Z + big  
				for i in range( left_3):
					answer = answer + t + big
				for i in range (left_1 ):
					answer = answer + s + big
				if len(answer) != num:
					print False ,2
					print len(answer)
					print num

		else:
			return  'IMPOSSIBLE'


	elif big_num ==2:
		if color[0] == color[2]:
			left =  big_value - color[4]
			for i in range( color[4]):
				answer = answer + 'BRY'
			for i in range (left):
				answer = answer + 'RY'
		elif color[2] == color[4]:
			left =  big_value - color[0]
			for i in range (color[0]):
				answer = answer + 'RBY'
			for i in range (left):
				answer = answer + 'BY'
		elif color[0] == (color[4]):
			left =  big_value - color[2]
			for i in range (color[2]):
				answer = answer + 'YBR'
			for i in range( left):
				answer = answer + 'BR'

		if len(answer) != num:
			print False,3
	elif big_num == 3:
		
		for i in range (big_value):
			answer =  answer + 'RBY'
		if len(answer) != num:
			print False,4
	# if len(answer) != num:
	# 	print False ,5
	# 	print len(answer)
	# 	print num

	print new_thing
	print answer


	if new_thing[0] == 1:
		eug = answer.index('B')
		answer = answer[:eug] + answer1 + answer[eug+1:]

	if new_thing[1] == 1:
		eug = answer.index('R')
		answer = answer[:eug] + answer2 + answer[eug+1:]

	if new_thing[2] == 1:
		eug = answer.index('Y')
		print answer1
		answer = answer[:eug] + answer3 + answer[eug+1:]

	return answer

	












case_num = 1
input_path = "../../Downloads/B-large-practice.in-2.txt"
out = open('new_color.txt', 'w')
with open(input_path) as f:
	lines = f.readlines()
	lines_head = lines[0]
	lines_body = lines[1:]
	for element in lines_body:
		input_element =  element.rstrip() # remove \n
		input_element_array = input_element.split()
		

		horse_num = map(int, input_element_array[1:])
		distant = sum(horse_num)
		
		number = fun(distant, horse_num)
		color = "Case #"+ str(case_num) +": "+ str(number)
		print(color)
		out.write(color+'\n')
		case_num = case_num +1


out.close()