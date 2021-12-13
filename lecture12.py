# coding=utf-8

"""
Useful sentence:
1. This ought to be good.
2. I want to look at one of those classes in a bit more detail because we're going to show you one new piece of the
    language.
3. There's a definition I'll put up on the screen.
4. I'm not going to go through the details, but you had the standard things you'd expect.
5. No post-docs (博士后)  are welcome. 不欢迎博士后
6. Is that a good idea?
7. Is that a not-so-good idea?
8. Is that a really bad idea?
9. Don't you hate professor who ask questions at 10 o'clock in the morning?
10. Well, I'm going to suggest that it's not a great idea, and here's why
11. So the last thing I want to show you here in this example, is let's look, in fact. right here.
12. I've added a method called allStudent.
    But it's a little different. I think, that things you've probably seen before.
13. So what do I mean by simulation methods?
14. First of all, let me talk about why do we want to get a simulation methods.
15. The idea was that there are going to be some places where it's really hard to build a model.
16. A highfalutin word.
17. So computation suddenly makes things change a lot.
18. So I did the following experiment this morning.
    - I went to Google, I could have gone to Bing, and I typed in "finance simulation." I got 5 million hits, most
        of them probably wrong by the way. And then finally, I typed in "Game simulation".
19. How many hits do you figure I got?
20. North or south of 15 million? North or south 指上下区间
21. It's really a common tool that we want to use here.
22. So let's think about what a simulation would look like, and then we're going to start building one.
23. Let me tell you what I mean by that.
24. It might actually be the case, by the way, that for ..... 实际上可能是这样
    - ... exactly the same scenario, I run the simulation multiple times and I might get slightly different answers.
25. as we said over here, 正如我们在这里所说的
26. Now probably the easiest way to think about this is, let's look at a model and a simulation.
27. I might not get a precise answer. I might not get the same answer every time. But if I do enough simulations of
    a circumstance (ˈsərkəmˌstans), I can get some good sense which I can refine of how this object's actually going to
    behave.
28. That's always a good start.


Vocabulary:
1. gobbledygook (ˈɡäbəldēˌɡo͞ok): language that is meaningless or is made unintelligible by excessive use
                                of abstruse technical terms; nonsense
2. store (stôr):
3. esoteric (ˌesəˈterik): intended for or likely to be understood by only a small number of people
                            with a specialized knowledge or interest.
4. constraint (kənˈstrānt): a limitation or restriction.
5. wrap up (rap): 圆满完成
6. macroscopic (ˌmakrəˈskäpik): 宏观的
7. tractable (ˈtraktəb(ə)l)
8. highfalutin (ˌhīfəˈlo͞otn):  (especially of speech, writing, or ideas) pompous (ˈpämpəs) or
                                pretentious (prəˈten(t)SHəs).（尤指演讲、写作或想法）自负的或自命不凡的。
9. refine (rəˈfīn): remove impurities(imˈpyo͝orədē: the quality or condition of being impure.)
                    or unwanted elements from (a substance), typically as part of an industrial process.
10. And of course, the last one is pretty obvious (ˈäbvēəs).
11. Put yourself back in the 1700s and think about how you would do a computation.
12. orrery (ˈôrərē): a mechanical model of the solar (ˈsōlər) system, or of just the sun, earth, and moon,
                        used to represent their relative positions and motions.
13. descriptive (dəˈskriptiv):serving or seeking to describe. 描述性的
14. prescriptive  (prəˈskriptiv): relating to the imposition or enforcement of a rule or method. 规定的
15. back and forth : noun An argument or discussion in which two or more people alternate in sharing their perspectives.
                    e.g. I think we should have a little back and forth before we make a final decision.
16. botanist (ˈbädənəst): an expert in or student of the scientific study of plants.
17. suspended in: 悬浮在
18. pretty straightforward:很简单; e.g. That's a pretty straightforward class.
19. wandering around: 四处流浪


"""

import datetime


class Person(object):  # Person was a subclass of

    def __init__(self, name):
        # create a person with name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1:]
        except:
            self.lastName = name
        self.brithday = None

    def getLastName(self):
        # return self's last name
        return self.lastName
        """                                      
            The next attribute, or the next metho
            >>I have that here because I don't wa
                self.lastName. That's part of the
            """

    def setBirthday(self, birthDate):
        # assumes birthDate is of type datetime.d
        # sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.brithday = birthDate
        """                                      
            >> setBirthday that gives values to i
        """

    def getAge(self):
        # assumes that self's birthday has been s
        # returns self's current age in days
        assert self.brithday != None
        return (datetime.date.today() - self.brit)

    def __lt__(self, other):  # It stands for les

        # return True if self's name is lexicogra
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name


class MITPerson(Person):  # i inherits the properties of the su
    nextIdNum = 0  # It's a class variable

    # the advantage of this is every time I get a new instance
    #  I can assign a unique ID. (Typically once we have classe
    #   global variables because we have these class variables,
    #    the same purpose in many cases)
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum  # An internal variabl
        MITPerson.nextIdNum += 1  # increment th ID number

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def isStudent(self):
        return type(self) == UG or type(self) == G


class UG(MITPerson):  # An UG, short for undergraduate
    def __init__(self, name):
        MITPerson.__init__(self, name)
        self.year = None

    def setYear(self, year):
        if year > 5:
            raise OverflowError("Too many")  # raise an overflow error
        self.year = year

    def getYear(self):
        return self.year()


class G(MITPerson):  # a graduate student
    pass  # means a G is an MIT person with no special properties
    # Q: Why did I introduce the type in thWell, I'm going to suggest that it's not a great idea, and here's whye first place?
    # A: Because it lets me do type checking, to check whether or not a person is a graduate student. (e.g. Type G)


class courseList(object):
    def __init__(self, number):
        self.number = number
        self.student = []

    def addStudent(self, who):
        if not who.isStudent():  # They're defensive programing;
            # checking using the inherited method to make sure that this person is actually a student
            raise TypeError("Not a student")
        if who in self.student:
            # self is pointing to the instance.students gives me the list of students currently in that instance.
            raise ValueError("Duplicate student.")
        self.student.append(who)

    def remStudent(self, who):
        try:
            self.student.remove(who)
        except:
            print str(who) + ' not in ' + self.number

    def allStudent(self):
        for s in self.student:
            yield s  # Here's the funky thing. I've used a word called yield.

    def ugs(self):
        indx = 0  # It's going to set index to 0.
        while indx < len(self.student):  # run through a while loop where it basically takes each student and
            if type(self.student[indx]) == UG:  # checks its type
                yield self.student[indx]
            indx += 1  # increment the index by 1
    # This is something you've seen before, taking a loop and walking along, taking each element of that list and saying
    # , if it's an undergraduate, I'm going to give you back that student, and I'm incrementing index at the bottom

    # def getStudent(self):
    #     return self.student

    # def __str__(self):
    #     result = ''
    #     for i in self.student:
    #         result = result + str(i) + ' '
    #     return result


m1 = MITPerson('Tianyuan Xu')
ug1 = UG('Jiahao Wu')
ug2 = UG('Linxin Tao')
g1 = G('Xuping Lu')
SixHundred = courseList('6.00')
SixHundred.addStudent(ug1)
SixHundred.addStudent(g1)
SixHundred.addStudent(ug2)
for i in SixHundred.allStudent():
    print i

"""
>>> print SixHundred
<__main__.courseList object at 0x7f68d4a637d0>
# So where are the students?
>> They're sitting down inside of an internal variable which is, in fact, in this case,
    the list of students.
    
# for x in SixHundred.student:
     print x
     
 Jiahao Wu
 Xuping Lu
 Linxin Tao

>>So I took the instance, I went in and pulled out an internal variable, and then I did a for loop that walked along it,
    printing those out.
# Well, I'm going to suggest that it's not a great idea, and here's why
>> I'm reaching into an instance and pulling out an internal variable and doing something with it.
>> A much cleaner way of dealing with that is to build an interface, to build a function, a method, that belongs to that
    instance, that would give me back the pieces I want.
    


# yield
>> I'm not directly accumulating a list. You don't see anywhere where I'm building up a list here.
    Yield is a generator. A generator is a little bit like a return, but with a big exception.
    If I had a return in that method somewhere, when it found the first thing, it's going to give me back the value
    and it's done. And so any information it stored about where it was in that computation. the phrase we use is it 
    gets popped off the stack frame
    - A generator is a function that remembers the point in the body where it last returned, plus all the local variable
    - The generator as something that keeps track of the state of the computation, so it can go back and pick it up 
        whenever it needs it.
        
# Analytic (ˌanəˈlidik) methods
    - predict behavior given some initial conditions and some parameters.
# Simulation methods.        
    - we have systems taht are not mathematically tractable.
        There are some systems where it's really hard to build a physical model that exactly predicts what's going to 
        happen. e.g. Think weather forecasting.
    - we're better off just successively refining a series of simulations.
        In other words, rather than spending the effort trying to build a very detailed predictive model, analytic
        model, just run a simulation that gives us an insight (ˈinˌsīt) to what the problem's doing.
    - easier to extract useful intermediate results from a simulation than it is to try and build a detailed analytic 
        model.
    - computers
    
# You can crank (kraNGk) it out by hand. Imagine how detailed a model you could actually do that way.
    Or you could build really precise detailed mechanical models.
    - mechanical orreries, which were these very complex pieces of clockwork that allowed you to try and predict the
        motions of the planets. That's a really expensive way to try and do a simulation.

# Simulation.
    - simulation means giving me an estimate, rather than prediction.
    - Giving me a sense of what might happen to a system under certain conditions and doing that multiple times,
        actually running, if you like, a model of the system rather than trying to predict exactly what's going to 
        happen. 
        
# Build a model. the following property.
    - give useful information about the behavior of a system.
    - give me approximation to reality (rēˈalədē).
    - simulation models are descriptive, not prescriptive
        e.g. With the simulation, it says, given a particular scenario (səˈnerēˌō), I can give you a good guess of
        what's going to happen.
    - Because maybe the world, as we said over here, is something that we can't model exactly mathematically.
        
# Analytic model
    - Analytic models are prescriptive. 
    - e.g. You type in the definition of the parameters of the problem and it would tell you, at least to the
        accuracy of computer, exactly what's going to happen.
        
# Talk about a story, the example
    -  I'm going to go back, again, a couple hundred years.
        In 1827, a Scottish (ˈskädiSH) [relating to Scotland or its people.] botanist named Robert Brown observed that
        a pollen (ˈpälən) [花粉] particle suspended in water seemed to just float at random.
        It's called Brownian motion, named after Robert Brown. He had no plausible (ˈplôzəb(ə)l) [(of an argument or 
        statement) instanceseeming reasonable or probable.] explanation for this. He just observed it. And he made no attempt to
        model it mathematically, which kinds of makes sense. That's 1827. The first really clear mathematical model of 
        Brownian motion didn't come around until 1900. A guy named Louis Bachelier had a doctoral thesis (ˈTHēsis) 
        called "The Theory of Speculation [the forming of a theory or conjecture without firm evidence.]"  Part of the
        problem for Bachelier, thoughc[despite (dəˈspīt) the fact that; although.], was that he didn't model Brownian 
        motion in pollen particles. He did it in finance markets. And that was considered, at least at the time,
        completely disreputable [声名狼藉; not considered to be respectable in character or appearance.]. And so nobody 
        paid any attention to his thesis. That's not going to happen to your thesis.....So it took eighty years to get
        to that point.
        
        Unfortunately, for poor Bachelier, five years later, another person came along and actually built the kind of
        model that introduced this sort of [In other words, people throw “sort of” into their speech because 
        they’re unsure. ; 有点]... what's called stochastic (stəˈkastik) [adj. randomly determined; having a random 
        probability distribution or pattern that may be analyzed statistically but may not be predicted precisely.] 
        thinking into the world of physics. This was a model that was almost exactly the same as Bachelier's, but it
        was used to confirm the existenceof atoms. Anybody know who did that model in 1905. No physics buffs [
        a person who is enthusiastically (ēnˌTH(y)o͞ozēˈastəklē) interested in and very knowledgeable about a 
        particular subject. ] here.  If I told you he was born in Switzerland, would that help? A minor guy named 
        Albert Einstein. So that was one of the first things Einstein did, was he actually built the first really good
        model of Brownian motion
        
        So Brownian motion is an example of a tool we're going to use a lot. It's an example of what we call a random
        walk.
        {I'm probabinstancely hiding that below the screen where you can't see it.} 
        
        -Random walks you're going to see all over the place. They're an incredibly useful way of building a simulation.
        And the essential idea of a random walk is, if I've got a system of interacting objects could be pollen 
        particles. I want to model what happens in that system under the assumption that each one of those things is
        going to move at each time step under some random distribution. I want to model what the overall system does.
        {Ok, let me give you some examples of where this is really useful.}
        {It's really useful in modeling physical processes}
        [any kind of + (singular noun)]
        {Well, we're going to start with pollen particles in air. But you could think about any kind of particle in 
        water. You could think about any kind of air particle in a larger fluid(ˈflo͞oid)}
        [No vacancy(ˈvākənsē): empty space.]
        Modeling weather, if we could really model the motion of all those molecules(ˈmäləˌkyo͞ol)[a group of atoms
        bonded together, representing the smallest fundamental unit of a chemical compound that can take part 
        in a chemical reaction.; 分子] is just a really large random walk.
        {Random walks are really useful in understanding biological processes}
        For example, the kinetics(kəˈnediks)[the branch of chemistry or biochemistry concerned with measuring and 
        studying the rates of reactions.; 动力学] of displacement [the moving of something from its place or position.
        : 移位;替换] of RNA [核糖核酸] from heteroduplexes (hedərəˈd(y)o͞oˌpleks) [异源双链体 ] of DNA is a great example of 
        a random walk. And in fact, people interested in bioinformatics [the science of collecting and analyzing complex 
        biological data such as genetic codes.] or computational biology will see random walks used all the time to try
        and to understand the displacements of things.
        {It's really useful in social processes} Movement of the stock market is definitely a random walk. Except for
        day when the markets are all crashing for unfortunate reason.
        
        In the example I'm going to use to motivate a random walk, we're going to build a simulation. Here is what was
        the traditional view of a random walk.
        
        {Let's take a drunken [drunk or intoxicated] university student. Not an Institute (ˈinstəˌt(y)o͞ot) [a society or
         organization having a particular object or common factor, especially a scientific, educational, or social one.]
        student, a University student}
        {So this is a Harvard student, not an MIT student, because I know you're well-behaved}
        {At least smile at me when I make these bad jokes.}
        You're got a drunken student. They're out on a big field. And they start off in the middle of the field, and 
        every second, this student can take one step in one of the four cardinal directions [The four cardinal 
        directions are north, south, east and west.] So north, south, east, west. After 1,000 seconds after 1,000 steps.
        Q: How far away is that student from where he or she started out? We'll make it a he. From where he started out.
        Guesses: It depends on the probability of what direction you're going.
        Q: Ok, so let's assume that the steps were equally likely [同样可能]. The four steps, north, south, east, west. 
        They're all equally probable.
        A: So the suggestion over here is, where he started. So 0 distance away.
        {That's not a bad guess, right?} You're just going in different directions. It's equally [ˈēkwəlē] likely you
         end up where you started. So one possibility is 0. You end up back where you started.
        {Well, I'm going to take bets here. This side of the crowd(kroud)[a large number of people gathered together in 
        a disorganized or unruly way.]. I don't want to just do the right side. I'm very liberal (ˈlib(ə)rəl).
        Somebody over on this side. Help me out. Boy, I get no eye contact when I do this. }
        {500 root 2. Can I drop the root 2 for second? The 500 is not a bad guess, right? Because you're about half the
        distance away. The root 2 we'll come back to in a second. Keep that in mind.}
        {Let's see if we can figure out what might happen here.}
        But before I do that, one of the good things to do is to try and build a simple that we could use to get an
        intuition about what's going to happen.
        
        So I'm going to start with a very simple model here. put x- and y-axes onto this field.
        We'll just call that the origin. It doesn't matter what it is, but that's where the students starts off. And 
        what I want to do is I want to get a very rough(rəf) sense of how far away the student might go after a few
        steps. We won't be able to go very far, but enough steps that we can start estimating this. So they start here.
        After one step, there are the places the student could end up. Equally likely, so after one step, if I want o
        build a distance associated probability. 
        
                            Distance,       Probability 
        - 1 step.           1               1
        Let's assume the student went east. In fact, they're all going to be roughly the same.
        And the second step, where can the student go? Well, in one out of four cases, he's at a distance 0, which would
        be back to where we started, which is that original pretty good guess.
        And if we went east agian, we're 2 units away
        - 2 step.           0               1/4
                            root 2          2/4 [2 out of 4 times]
                            2               1/4 [with probability 1 in 4.]
        {I'm cheating slightly here, in the sense that I should do the same things if the first step was north, south,
        or west, but they're all symmetric (səˈmetrik)[made up of exactly similar parts facing each other or around an 
        axis(ˈaksəs); symmetrical.] to this. So it'll all come out the same way.
        There is what happens after two steps.
        - 3 step.           1               1/4
                            1               1/4
                            root 5          1/4
                            3               1/16
                            1               1/16
                            root 5          1/8
        About three possibilities, If I'm in this case, which is the 0 case, I'm here, in which case no matter which 
        step I take, I'm 1 unit away.
        {Let me put that over here. You can kind of do the math in your head}
        Q: What's the expected distance away?
            What's the average distance I'd be away?
            
        -   1 step:             1
        -   2 step:             about 1.2
        -   3 step:             about 1.4 or 1.5
        {Let me make it 1.4. It's probably a little bit closer.}
        Q: Why was I doing that?
        This is something you want to do as you start building a simulation, which is do a little bit of a calculation 
        to get a sense of what you expect to happen here.
        >> So what conclusion could I draw from that?
        Admittedly(ədˈmididlē)[used to introduce a concession or recognition that something is true or is the case.] on
        very small numbers, it looks like the more steps the Harvard student takes, on average the further away they are 
        from the starting point. So your 0 was a great guess, but it's probably not going to work here.
        
    -   I just take those distances squared and take the square root of them. It's just giving me distance away, which 
        is pretty nice.
        {And that method is the one up here called move}
        {So the background to this is going to have a drunk at at a location. One of the things I will want is to be
        able to change location, So move says, if you give me a change in x and a change in y. I'm going to assume 
        they're floats(flōt). I will give you back the new location, which is to go from my x and y by some amount.}
    
        Move method: It returns a new instance of a location.
        
        {I made a couple of assumptions which are worth thing about here}
        {So one assumption is I'm assuming that this is a 2D world. You can't elevate, you can't rise up.
        There's no change in altitude. That kind of makes sense.
        The second assumption I made was I said, I want to build it in so that things like delta-x and delta-y are 
        floats. What is that doing? That's saying, I don't want to restrict myself to just moves that are only in the
        cardinal directions. I'm going to start there, but initially, I'd like to have the ability that the move could
        be along a diagonal, or it could be some partial step. So notice I'm making a choice there that is kind of nice.
        }
        {So the second thing I need is I need to say, what's a field going to be?
        I want to show you that definition, which is right here.
        And a field is basically going to be something that maps drunks to locations. So a filed is just going to be a
        collection of drunks. Keep track of where they are. So let's look at what that definiton says.
"""

import random


class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}  # Dictionary

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)

    def __str__(self):
        return 'This drunk is named' + self.name


def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalk(numSteps, numTrials):
    homer = Drunk('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numTrials))
    return distances


def drunkTest(numTrials):
    for numSteps in [10, 100, 1000, 10000, 1000000]:
        distances = simWalk(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print '  Mean = ', sum(distances) / len(distances)
        print '  Max  = ', max(distances), '  Min =', min(distances)

def test():
    Tianyuan = Drunk('Tianyuan')
    origin = Location(0, 0)
    f1 = Field()
    f1.addDrunk(Tianyuan, origin)
    print walk(f1, Tianyuan, 10)

test()