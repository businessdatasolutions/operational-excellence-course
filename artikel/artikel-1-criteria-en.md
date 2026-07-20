# An agent only builds what you wrote down

*Part 1 of two. This part is about what a programme has to write down. [Part 2](artikel-2-docent-en.md) is about what the teacher gets out of it.*

Every programme is experimenting with AI by now. That is no longer a gamble, it is simply where we are. There are pilots, there are working groups, there is a framework document, there are lecturers who put something together on a Saturday morning that can go into Monday's class. The question of whether we are going to do this is settled.

Only: look at what comes out. A generator that produces multiple-choice questions from a chapter. A simulation that stands apart from everything else. A demo app that shines at a study afternoon and never launches again. Two years of experimenting, and educational quality has not moved a millimetre. The test goes out the door faster; the conversation with the student is the same conversation as in 2019.

What is missing?

Not the technology, and not the willingness either. What is missing are the design criteria: written down explicitly and machine-readable. An AI agent can only build what you wrote down. Higher education never wrote down what good education is. So it gets test generators back.

I can show you that rather than assert it. The screens in this piece come from a module I rebuilt this year, and that system was not made by a development team. It was designed and written by an AI coding agent. My work was the steering: first a Learner Requirement Document, the pedagogical design, before a single line of code existed. After that I supplied background material, ideas and corrections, and made the calls where that document was silent. The agent built what was in it. That is not an anecdote alongside this article. It is the evidence underneath it.

A note on the screenshots: the interface is Dutch throughout. This is the system as our students actually use it.

## Write nothing down and you get micro-tasks back

I have seen enough of these outputs by now to recognise a pattern. MC generators, stand-alone simulations, chatbots that can quote the course guide. They share something that is rarely named: the only criteria they ask for are criteria about themselves.

Take that test generator. Ask a model for ten multiple-choice questions on a chapter and you get ten questions whose distractors are transparent, two of which test the same thing, and whose correct answer is suspiciously often the longest one. It only becomes usable once you write down what a good item is: one defensible key, distractors that represent a mistake students actually make, no cues in the phrasing, no question you could answer without having read the chapter. Do that, and it works. Out come questions you would put in a test without wincing.

And notice where those rules had to come from: nowhere. What makes a good distractor, how you keep a key defensible, why a question you can answer without the chapter is not a question: all of that sat in the heads of people who have been constructing tests for twenty years. We never wrote it down, because we trusted their craft. And rightly so. Only when we tried to explain it to a machine did it turn out we did not have it.

Now look at what kind of criteria those are. Every one of them is about the item itself. They say nothing about why this concept sits in week 3 and not week 7, what prior knowledge it assumes, which misconception students reliably have here, or how the answer connects to what happens in the final assessment. You can write a flawless multiple-choice question about a chapter that is in the wrong block.

That is the whole thing. The criteria you supply set the ceiling on what you get back. Supply rules about item quality and you get good items: exactly that, and nothing above it. About coherence, sequence and build-up you get nothing, and not because the agent could not do it. Because nobody wrote it down. The micro-task is therefore not a modest first step towards something bigger. It is the ceiling of the criteria you had.

To be clear: that generator is not bad. It does what it promises. It just promises nothing about educational quality, and we treat it as though it does.

## Some of it is already written down, in the book you are throwing out

Here is the turn I miss in most AI conversations in education. We act as though design criteria still have to be written, and as though that is a three-year academic project. Meanwhile, part of it is already sitting on your desk.

A good textbook is written by someone who knows three things. What is relevant within a field of knowledge and what is not. How the parts hang together. And in what order you study them, so that the second understanding can rest on the first. Open the table of contents: that is sequence plus coherence, and those are design criteria. The rest comes on top of it. The didactic notes beside a chapter. The worked cases, chosen because they sharpen one specific distinction. The discussion questions at the back, often written more precisely than the learning outcomes in our own module handbook.

Writing the book off as an expensive content carrier is the same mistake as commissioning a demo app. Both throw away what was explicit and keep only the text. The book is not expensive because of the paper. It is expensive because of the ordering, and that ordering is the one thing an agent can read.

With us that did not stay a metaphor. The module's knowledge base is a public wiki at its own address, and it is not thematically ordered by something that invented a structure of its own. It follows the book's chapters, and shows each team what fits where they currently stand.

![](figures/fig-01-wiki.png)

**Figure 1.** (1) The wiki is ordered by the textbook's chapters, tagged as book concepts. That numbering is the sequence the author chose, and the system adopts it instead of inventing its own. (2) A concept the teacher added, with no chapter number. The book supplies the structure, the teacher adds to it. (3) And this page the system wrote itself, from a video the teacher pointed it at. All three appear here because the team is in this phase: the wiki shows what fits where they now stand.

Notice what the system is not doing here. It invents no thematic scheme of its own, it writes no summary of the book, it ranks nothing by a relevance it worked out for itself. It adopts the ordering an expert put there, and filters within it. That is not a limitation I had to accept. It is the reason it works.

## Write it down and the agent will build it

And then the third claim, which turns the first two around. Once the criteria are there, in a form a machine can read, something happens that the micro-task never delivers.

In this system a single JSON file decides which model fills which role. That same line is the text the student reads on screen. Not two sources that can drift apart: one source, two readers.

![](figures/fig-02-transparantie.png)

**Figure 2.** (1) A single JSON file decides which model fills which role. That same line is the text the student reads here. (2) "This list is not a snapshot someone maintains by hand. It is the exact configuration the system runs on. Change a model and this table changes with it, or the system refuses to start."

That last sentence is the whole point. The system refuses to start if the promise made to the student and the reality drift apart. That is not a programmer being careful, it is a requirement somebody wrote down.

The same holds for something far less technical. Write down that quality emerges at several moments rather than at one moment at the end, and it stops being vision-speak. It becomes four phases with two gates at each: a Socratic AI tutor, and a peer partner team that reads another team's work.

![](figures/fig-03-tutor.png)

**Figure 3.** (1) The four phases, each with its own gate. Design is finished, Direct is still open: quality is tested at several points, not at a single moment at the end. (2) "Socratic questions only: never a score or verdict visible to the team." That rule does not sit in a manual, it sits above the conversation, and the report below it obeys. (3) A real question from the tutor about this team's Ryanair case. The tutor probes what the team wrote down itself, and nowhere supplies the answer.

The most striking thing about that report is what is not in it. No grade, no verdict, no "well done, just watch out for". Only questions that reach back into the team's own words: the 25-minute turnaround, the point-to-point flights, its own claim about Industry 5.0.

So that tutor is not a chatbot. There is no dialogue and the student cannot talk back to it. That is not a shortcoming we still have to fix; it is written down, because a tutor you can negotiate with is no longer a gate. The agent that built this honoured that in a place where nobody would have checked.

## What this means for your next pilot

Three things, and they stand independently. Supply no criteria and you get back work from the only category that runs without them. Some of your criteria you already have, in the book you are considering dropping. And write them down, and an agent will hold to them, including where they get in its way.

So if your programme runs another AI pilot next year, ask one question before anything gets built. Which criteria are we handing over, and where are they written down? If the answer is "our lecturers know that", then the answer is "nowhere", and you already know what you will get back. Start with the book you have already prescribed, because someone there did the work we have spent twenty years walking around. The problem was never that the machine does not understand us. It is that we never wrote it down.

*In [part 2](artikel-2-docent-en.md): what the teacher gets out of this, and why the return is cognitive rather than administrative.*
