def get_user_input():
  """Gets user input for note, octave, and duration.

  Returns:
    A tuple containing the note, octave, and duration.
  """
  note = ''
  octave = -1
  duration = -1
  
  while True:
    note = input("Enter the note (A, A#, B, C, C#, D, D#, E, F, F#, G, G#): ").upper()
    if note in ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']:
      break
    else:
      print("Invalid note. Please try again.")

  while True:
    try:
      octave = int(input("Enter the octave (0-8): "))
      if 0 <= octave <= 8:
        break
      else:
        print("Invalid octave. Please enter a number between 0 and 8.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  while True:
    try:
      duration = float(input("Enter the duration (0-6 seconds): "))
      if 0 <= duration <= 6:
        break
      else:
        print("Invalid duration. Please enter a number between 0 and 6.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  create_sample(note, octave, duration)
  
  return 