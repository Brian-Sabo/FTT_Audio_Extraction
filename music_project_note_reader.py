## new program to store notes
import winsound as w



class sheet:
    def __init__(self,lines):
        self.paper = lines
    
    def data(self):
        for i in range(len(self.paper)):
            print("line", i+1)
            self.paper[i].data() 
    
    def play(self):
        for i in range(len(self.paper)):
            self.paper[i].play()
    
    def shift(self,amount):
        for i in range(len(self.paper)):
            self.paper[i].shift(amount)

class line:
    def __init__(self,bars):
        self.group = bars
    
    def data(self):
        for k in range(len(self.group)):
            print("measure", k+1)
            self.group[k].data()
    
    def play(self):
        for k in range(len(self.group)):
            self.group[k].play()
    
    def shift(self,amount):
        for k in range(len(self.group)):
            self.group[k].shift(amount)
            
class measure:
    total = 4           #make the total base on time sig
    
    def __init__(self,bar):
        self.notes = bar     #copys data from input into class
        self.size = len(self.notes)
        
    def data(self):
        for i in range(self.size):
            print(self.notes[i].name, end=" ")
            print("note", i+1)
    
    def play(self):
        for i in range(self.size):
            w.Beep(round(self.notes[i].freq), round(self.notes[i].time_120))
            #winsound is w beeping the notes
    
    def shift(self,amount):
        for note_index in range(self.size):
            self.notes[note_index].new_pitch = (self.notes[note_index].general_pitch + amount)
            self.notes[note_index].update_pitch()
            
       
        
class note:
    base_freq = 440     #440 hz A
    
    def __init__(self,name,time):
        self.name = name    # constructor initalzaiton
        self.freq = self.name2freq()
        self.time = time
        self.time_120 = self.time_2_120()
        self.general_pitch = self.get_general_pitch()
        self.new_pitch = 0              #will be updated in shift method
        self.shifted_pitch = self.update_pitch()
        print(self.name, "the freq is", self.freq, "the length is", self.time, "\n")
    
    def gettime(self):
        return self.time
    
    def get_general_pitch(self):
        global pitch_up, pitch_down
        pitch_up = ["C3","C#3","D3","D#3","E3","F3","F#3","G3","G#3","A3","A#3","B3","C4","C#4","D4","D#4","E4","F4","F#4","G4","G#4","A4","A#4","B4","C5","C#5","D5","D#5","E5","F5","F#5","G5","G#5","A5","A#5","B5"]
        pitch_down = ["C3","Db3","D3","Eb3","E3","F3","Gb3","G3","Ab3","A3","Bb3","B3","C4","Db4","D4","Eb4","E4","F4","Gb4","G4","Ab4","A4","Bb4","B4","C5","Db5","D5","Eb5","E5","F5","Gb5","G5","Ab5","A5","Bb5","B5"]
        for pitch_val in range(len(pitch_up)):
            if self.name == pitch_up[pitch_val]:
                return pitch_val
        ## if note is not in the pitch it is a flat so
        for pitch_val in range(len(pitch_down)):
            if self.name == pitch_down[pitch_val]:
                return pitch_val
    
    def update_pitch(self):
        invalid_shift = True
        if self.new_pitch > 0 and self.general_pitch < self.new_pitch and self.new_pitch < len(pitch_up):
            self.name = pitch_up[self.new_pitch]
            self.freq = self.name2freq()
            invalid_shift = False
            print("the shifted up note is ", pitch_up[self.new_pitch], "shifted by ", self.new_pitch - self.general_pitch, "with a new freq of ", self.freq)
            
        
        if self.new_pitch > 0 and self.general_pitch > self.new_pitch and self.new_pitch < len(pitch_down):
            self.name = pitch_down[self.new_pitch]
            self.freq = self.name2freq()
            invalid_shift = False
            print("the shifted down note is ", pitch_up[self.new_pitch], "shifted by ", self.new_pitch - self.general_pitch, "with a new freq of ", self.freq)
        
        if invalid_shift:
            print("the note can't be shifted down or up it is out of range of C3-B5")
        
    def time_2_120(self):    #sets to 120 tempo quarter note
        return (60000/120)*self.time
        # 60000 ms/ 120 bpm * value 1 for quater 2 for half etc
    
    def name2freq(self):                                        ## will take the note name and return the freq
        
        notelist4 = list(range(12))
        notelist3 = notelist5 = notelist4                       ##arrays of freq for notes
        notelist3 = [130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94]
        notelist4 = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88]
        notelist5 = [523.25, 554.37, 587.33, 622.25, 659.26, 698.46, 739.99, 783.99, 830.61, 880.00, 932.33, 987.77]
        match self.name:
            ## ocatve 3
            case "C3":
                return notelist3[0]
            case "C#3" | "Db3":
                return notelist3[1]
            case "D3":
                return notelist3[2]
            case "D#3" | "Eb3":
                return notelist3[3]
            case "E3":
                return notelist3[4]
            case "F3":
                return notelist3[5]
            case "F#3" | "Gb3":
                return notelist3[6]
            case "G3":
                return notelist3[7]
            case "G#3" | "Ab3":
                return notelist3[8]
            case "A3":
                return notelist3[9]
            case "A#3" | "Bb3":
                return notelist3[10]
            case "B3":
                return notelist3[11]
            ## ocatve 4
            case "C4":
                return notelist4[0]
            case "C#4" | "Db4":
                return notelist4[1]
            case "D4":
                return notelist4[2]
            case "D#4" | "Eb4":
                return notelist4[3]
            case "E4":
                return notelist4[4]
            case "F4":
                return notelist4[5]
            case "F#4" | "Gb4":
                return notelist4[6]
            case "G4":
                return notelist4[7]
            case "G#4" | "Ab4":
                return notelist4[8]
            case "A4":
                return notelist4[9]
            case "A#4" | "Bb4":
                return notelist4[10]
            case "B4":
                return notelist4[11]
            ## ocatve 5
            case 'C5':
                return notelist5[0]
            case "C#5" | "Db5":
                return notelist5[1]
            case "D5":
                return notelist5[2]
            case "D#5" | "Eb5":
                return notelist5[3]
            case "E5":
                return notelist5[4]
            case "F5":
                return notelist5[5]
            case "F#5" | "Gb5":
                return notelist5[6]
            case "G5":
                return notelist5[7]
            case "G#5" | "Ab5":
                return notelist5[8]
            case "A5":
                return notelist5[9]
            case "A#5" | "Bb5":
                return notelist5[10]
            case "B5":
                return notelist5[11]
                
        
    
def load(filename):
    file = open(filename, "r")
    sheet_file = file.readlines()
    #print(sheet_file[0])
    #print(sheet_file[1])
    #print(sheet_file[2])
    
    ## loads time and note name into arrays from txt file
    time_index = []
    all_notes = []
    space_index_0 = [-1]          #to start the index
    space_index_1 = [-1]
    count_space_index = 0
    index = 0
    for sheet_line in range(2):
        for char in sheet_file[sheet_line]:
            if char.isspace():
                if sheet_line == 0:
                    space_index_0.append(index)
                    all_notes.append(sheet_file[0][space_index_0[count_space_index]+1:index])
                if sheet_line == 1:
                    space_index_1.append(index)
                    time_index.append(float(sheet_file[1][space_index_1[count_space_index]+1:index]))
                count_space_index += 1      #index indices arr
            index += 1          # to count indices space
        index = count_space_index = 0 # to rst for second load
    
    #print(space_index_0,space_index_1)
    #print(all_notes,time_index)
    
    note_count = len(time_index)

    ## to intailize measures and notes
    temp_line = []
    temp_measure = [],[],[],[],[],[],[],[],[],[] #need to fix later
    #to allow for more than 10 measure heap?
    #print(type(temp_measure))
    overflow_time, current_note, total_time = 0, 0, 0
    time_max = 4     #should get from time sig
    temp_index = 0
    while current_note < note_count:
        total_time += time_index[current_note]
        #print(all_notes[current_note])
        O1 = note(all_notes[current_note], time_index[current_note])
        temp_measure[temp_index].append(O1)   #add note to note arr
        #print(total_time)
        current_note += 1
        if total_time >= time_max:
            global M1
            M1 = measure(temp_measure[temp_index])
            print("NEXT MEASURE")
            temp_line.append(M1)
            overflow_time = total_time - time_max
            total_time = 0 + overflow_time
            if current_note != note_count:
                temp_index += 1        #fix later
                #print(temp_index)
            #rst the time and measure
    global L1, S1
    L1 = line(temp_line)
    S1 = sheet([L1])
    #fixed
    
def main():     
    #print("name that note put Bb for bflat, and A# for a_sharp")
    print("\nEnter the file name of the sheet to load:")
    load(input())
    print("the whole song is \n")
    S1.data()
    print("\nwould you like to play hear the song\n 1 for yes, 2 for no")
    usr_in = input()
    if usr_in == '1':
        S1.play()
    elif usr_in == '2': 
        print("exiting")
        w.PlaySound("SystemExit",w.SND_ALIAS)
    print("would you like to shift the song?\n 1 for yes")
    usr_in = input()
    if usr_in == '1':
        print("enter the shift in the number of tones each ocatve has 12 tones use - to shift down and + to shift up")
        S1.shift(int(input()))
        print("the shifted song is\n")
        S1.data()
        S1.play()
        
main()
