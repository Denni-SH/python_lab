
from os import path,rename
import shutil
import glob
import threading
import argparse


def parcing():
	parser = argparse.ArgumentParser()
	parser.add_argument('--operation', choices=["copy", "move"], help="Choose operation: copy or move")
	parser.add_argument('--from_path', help="Enter path", type = str)
	parser.add_argument('--to_path', help="Enter destination path")
	parser.add_argument('--threads', default=1, help="Enter count of threads",type = int)
	args = parser.parse_args()
	return args


def move_file(prev_name,next_name):
	rename(prev_name,next_name)
	print('replaced file from %s to %s' %(prev_name,next_name))


def copy_file(prev_name,next_name):
	shutil.copy(prev_name,next_name)
	print('copied file from %s to %s' %(prev_name,next_name))


def move_dir(prev_dir,next_dir):
	shutil.move(prev_dir,next_dir)
	print('replaced dir %s to %s' %(prev_dir,next_dir))


def copy_dir(prev_name,next_name):
	shutil.copytree(prev_name,next_name)
	print('copied dir from %s to %s' %(prev_name,next_name))


def mask_copy(prev_dir, next_dir, file, event_for_wait, event_for_set):
	event_for_wait.wait() # wait for event
	event_for_wait.clear() # clean event for future	
	# print('agas')
	shutil.copy(file,next_dir)
	# print('file %s was copied in %s' %(file,next_dir))
	event_for_set.set() # set event for neighbor thread


def f_thread(thread_count,from_path,to_path):
	events = []
	threads = []
	if thread_count > len(glob.glob(from_path)):
		thread_count = len(glob.glob(from_path))
	# init events
	for i in range(thread_count):
		new_event = threading.Event()
		events.append(new_event)
	# init threads
	for file in glob.glob(from_path):
		for num in range(thread_count):
			if num != thread_count - 1:
				new_thread = threading.Thread(target=mask_copy, args=(from_path,to_path, file, events[num], events[num+1]))
			else:
				new_thread = threading.Thread(target=mask_copy, args=(from_path,to_path, file, events[num], events[0]))
			threads.append(new_thread)
	# start threads
	for thread in threads:
		thread.start()
	# initiate the first event
	events[0].set() 
	# join threads to the main thread
	for thread in threads:
		thread.join()

def processing(operation,from_path,to_path,threads):
	if  path.exists(str(to_path[0])) or path.exists(to_path) and path.exists(str(from_path[0])):
		
		if operation == 'copy':
			if path.isdir(from_path) == True:
				if not path.exists(to_path):
					copy_dir(from_path,to_path)
				else:
					print('already copied')
			elif path.isfile(from_path) == True:
				copy_file(from_path,to_path)
			else:
				if not path.exists(from_path) and not path.exists(str(from_path[0])):
					print('There`s not this from_path!')
				else:
					f_thread(threads,from_path,to_path)
		elif operation == 'move':
			if path.isdir(from_path) == True:
				move_dir(from_path,to_path)
			elif path.isfile(from_path) == True:
				if not path.exists(to_path):
					move_file(from_path,to_path)
				else:
					print('File already moved!')
			else:
				print('There`s not this from_path!')
		else:
			print('There`s not this operation! Enter again.')
	else:
		print('There`s no this path! Enter again.')


if __name__ == '__main__':
	args = parcing()
	processing(args.operation,args.from_path,args.to_path,args.threads)
