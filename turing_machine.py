import set_internal_states_table as sist

## References
# https://sandipanweb.wordpress.com/2020/08/08/simulating-a-turing-machine-with-python-and-executing-programs/
# https://stackoverflow.com/questions/59045832/turing-machine-for-addition-and-comparison-of-binary-numbers

N = 1000 # tape length, initialize to a large value
 
class TuringMachine:
    def __init__(self, algo, input, state=0):
            # init dict
        self.trf = {}
            # state to string
        self.state = str(state)
            # init tape with underscores
        self.tape = ''.join(['_']*N)
            # set head position
        self.head = N // 2   # head is in the middle
            # insert input into the middle of the tape
        self.tape = self.tape[self.head:] + input + self.tape[:self.head]
        print('\nInternal states table')    
        print('---------------------')
            # assign value to key
        for line in algo.splitlines(): # for each line in the internal states table
                # s, s1: current state and next state; d: shift direction; 
            s, a, r, d, s1 = line.split(',') # a: value read; r: value write
            self.trf[s, a] = (r, d, s1) # current state and accept value
            print(line)
            print('---------')


    def shift_one_step(self, i):
            # H means halt
        if self.state != 'H':
                # assert self.head >= 0 and self.head < len(self.tape) here
            a = self.tape[self.head]
                # get current state based on state and a (value read)
            action = self.trf.get( (self.state, a) )
            
            if action: # if action = (r0, d0, s1_0)
                    # assign r = r0, d = d0, s1_0
                r, d, s1 = action
                    # insert input into tape
                self.tape = self.tape[:self.head] + r + self.tape[self.head+1:]
                    # move head and shift state
                if d != '*':
                    self.head = self.head + (1 if d == 'r' else -1)
                    self.state = s1
                    print(str(i+1) + ' ' + self.tape.replace('_', ''), self.state)
                    print('---------')


    def execute(self, max_iter=10000):
        print('\ni in   state')
        print('------------')
        i = 0
            # execute through the tape
        while self.state != 'H' and i < max_iter: # prevent infinite loop
            self.shift_one_step(i)
            i += 1
            # clear the tape
        res = self.tape.replace('_', '')    
        print('\nRESULT')
            # results output
        print("{} + {} = {} (binary)".format(first_bin_num, second_bin_num, res))
        print("{} + {} = {} (decimal)".format(int(first_bin_num, 2), int(second_bin_num, 2), int(res, 2)))


if __name__ == '__main__':    
        # header
    print("Adding two binary numbers x + y")
        # take inputs
    first_bin_num = str(input("x = "))
    second_bin_num = str(input("y = "))
    input = first_bin_num + '_' + second_bin_num
        # read internal states table
    algo = open(sist.sum_of_two_binary_numbers).read()
        # execute Turing machine
    turing = TuringMachine(algo, input)
    turing.execute() 
       