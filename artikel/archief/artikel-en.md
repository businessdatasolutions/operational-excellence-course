# An agent only builds what you wrote down

Every programme is experimenting with AI by now. That is no longer a gamble, it is simply where we are. There are pilots, there are working groups, there is a framework document, there are lecturers who put something together on a Saturday morning that can go into Monday's class. The question of whether we are going to do this is settled.

Only: look at what comes out. A generator that produces multiple-choice questions from a chapter. A simulation that stands apart from everything else. A demo app that shines at a study afternoon and never launches again. Two years of experimenting, and educational quality has not moved a millimetre. The test goes out the door faster; the conversation with the student is the same conversation as in 2019.

What is missing?

Not the technology, and not the willingness either. What is missing are the design criteria: written down explicitly and machine-readable. An AI agent can only build what you wrote down. Higher education never wrote down what good education is. So it gets test generators back.

## Micro-tasks are not a strategy, they are a symptom

I have seen enough of these outputs by now to recognise a pattern. MC generators, stand-alone simulations, chatbots that can quote the course guide. They share something that is rarely named: the only criteria they ask for are criteria about themselves.

Take that test generator. Ask a model for ten multiple-choice questions on a chapter and you get ten questions whose distractors are transparent, two of which test the same thing, and whose correct answer is suspiciously often the longest one. It only becomes usable once you write down what a good item is: one defensible key, distractors that represent a mistake students actually make, no cues in the phrasing, no question you could answer without having read the chapter. Do that, and it works. Out come questions you would put in a test without wincing.

And notice where those rules had to come from: nowhere. What makes a good distractor, how you keep a key defensible, why a question you can answer without the chapter is not a question — all of that sat in the heads of people who have been constructing tests for twenty years. We never wrote it down, because we trusted their craft. And rightly so. Only when we tried to explain it to a machine did it turn out we did not have it.

That is this entire article in miniature. The generator works precisely because somebody made tacit knowledge explicit. And it stays small because we only did that for the item.

Because look at what kind of criteria those are. Every one of them is about the item itself. They say nothing about why this concept sits in week 3 and not week 7, what prior knowledge it assumes, which misconception students reliably have here, or how the answer connects to what happens in the final assessment. You can write a flawless multiple-choice question about a chapter that is in the wrong block.

That is the whole thing. The criteria you supply set the ceiling on what you get back. Supply rules about item quality and you get good items: exactly that, and nothing above it. About coherence, sequence and build-up you get nothing — not because the agent could not do it, but because nobody wrote it down. The micro-task is therefore not a modest first step towards something bigger. It is the ceiling of the criteria you had.

To be clear: that generator is not bad. It does what it promises. It just promises nothing about educational quality, and we treat it as though it does.

## Design criteria are the work, and the textbook is a source of them

Here is the turn I miss in most AI conversations in education. We act as though design criteria still have to be written, and as though that is a three-year academic project. Meanwhile, part of it is already sitting on your desk.

A good textbook is written by someone who knows three things. What is relevant within a field of knowledge and what is not. How the parts hang together. And in what order you study them, so that the second understanding can rest on the first. Open the table of contents: that is sequence plus coherence, and those are design criteria. The rest comes on top of it. The didactic notes beside a chapter. The worked cases, chosen because they sharpen one specific distinction. The discussion questions at the back, often written more precisely than the learning outcomes in our own module handbook.

Writing the book off as an expensive content carrier is the same mistake as commissioning a demo app. Both throw away what was explicit and keep only the text. The book is not expensive because of the paper. It is expensive because of the ordering — and that ordering is the one thing an agent can read.

Before I go on, something you need in order to weigh the rest. The system you are about to see was not built by a development team. It was designed and written by an AI coding agent. My work was the steering: first a Learner Requirement Document, the pedagogical design, before a single line of code existed. After that I supplied background material, ideas and corrections, and made the calls where that document was silent. The agent built what was in it. That is not an anecdote alongside this article. It is the evidence underneath it.

And briefly, what that gets you, because I am about to pull individual screens out of it. The system has four parts. A **wiki** holding the knowledge base, ordered by the book's chapters. Not an internal database but a real, public wiki at its own address, which I maintain with an AI agent: businessdatasolutions.github.io/oe-wiki. A **student portal** where teams submit a checkpoint per phase. **Two gates** at every checkpoint: a Socratic AI tutor and a peer partner team. And a **teacher zone** with a dashboard, a student dossier and a quality report.

One thing holds them together. Every action is recorded as a fact: a team submits, the tutor reads and asks its questions, the gate opens or stays shut, the partner team does the same. With both gates open, the next phase unlocks. The teacher sees those same events again, summarised on the dashboard and spelled out in the dossier. Meanwhile the wiki decides what a team gets to read right now. Four phases, eight gates (four for the tutor, four for the partner teams), one trail of facts underneath.

With us that did not stay a metaphor. The knowledge base our students work with is not thematically ordered by something that invented a structure of its own. It follows the book's chapters, and shows what fits where the team currently stands.

![](figures/fig-01-wiki.png)

**Figure 1.** The interface is Dutch throughout: this is the system as our students actually use it. (1) The wiki is ordered by the textbook's chapters, tagged as book concepts. That numbering is the sequence the author chose, and the system adopts it instead of inventing its own. (2) A concept the teacher added, with no chapter number. The book supplies the structure, the teacher adds to it. (3) And this page the system wrote itself, from a video the teacher pointed it at. All three appear here because the team is in this phase: the wiki shows what fits where they now stand.

Once you write those criteria out in a form a machine can read, something happens that the micro-task never delivers. In our system a single JSON file decides which model fills which role, and that same line is the text the student reads on screen. Not two sources that can drift apart: one source, two readers.

![](figures/fig-02-transparantie.png)

**Figure 2.** (1) A single JSON file decides which model fills which role. That same line is the text the student reads here. (2) "This list is not a snapshot someone maintains by hand. It is the exact configuration the system runs on. Change a model and this table changes with it, or the system refuses to start."

That principle reaches further than compliance. Write down that quality emerges at several moments in the journey rather than at one moment at the end, and it stops being vision-speak. It becomes four gates, each at its own moment, that an agent can staff.

And then there is the question you can only ask once the criteria are written down. Not just the delivery becomes testable, but the design itself. Do the checkpoints cover the concepts the book marks as core? Is there a concept in week 6 that never returns in an assignment? That is not a question about students. That is a question about me.

My system does not work that out for me, by the way. I have not built that analysis, and I will not pretend otherwise. But the question is now askable, because there is finally something to hold it against. Five years ago there was nothing — not because it was forbidden, but because the answer lived in the heads of fourteen lecturers.

## The return is cognitive, not administrative

The pitch for AI in education is almost always time saved. That is the weakest version of the argument, and the version a room of teachers rightly distrusts.

Our AI tutor is the first gate, not the lecturer's replacement. It reads a submitted checkpoint and writes one report. That is all: it is emphatically not a chatbot, there is no dialogue, and the student cannot talk back to it. That is not a shortcoming we still have to fix. It is written down, because a tutor you can negotiate with is no longer a gate.

![](figures/fig-03-tutor.png)

**Figure 3.** (1) The four phases, each with its own gate. Design is finished, Direct is still open: quality is tested at several points, not at a single moment at the end. (2) "Socratic questions only: never a score or verdict visible to the team." That rule does not sit in a manual, it sits above the conversation, and the report below it obeys. (3) A real question from the tutor about this team's Ryanair case. The tutor probes what the team wrote down itself, and nowhere supplies the answer.

The most striking thing about that report is what is not in it. No grade, no verdict, no "well done, just watch out for". Only questions that reach back into the team's own words: the 25-minute turnaround, the point-to-point flights, their own claim about Industry 5.0. That is a Socratic tutor holding to its definition — and that definition was in the design document before any model was involved.

So what the team gets back are the questions, plus whether the gate is open or not. A grade it does not see: the rubric score stays hidden and goes to the lecturer.

![](figures/fig-04-dashboard.png)

**Figure 4.** (1) This screen is in its demo state too, and says so itself. What sits underneath is built: the route exists, and against a real class it returns real figures. (2) "Hidden score": the grade the student never sees and the teacher does. Not because it worked out that way, but because the team-facing report structurally has no field a score could go in. (3) The teacher can overrule the AI's gate. The server records every override in an audit trail, and refuses one that carries no stated reason: an override nobody can explain later is exactly what a student would ask about.

There is the answer to the question every teacher asks about an AI gate: who has the last word? The teacher does. They can open a gate the tutor held shut. But not quietly, and not without a reason. That an override requires a written justification is not a tidy afterthought: it is in the requirements, so the server refuses one without it. The button above it cannot even reach that server yet, and the rule already holds.

For the final assessment that lecturer gets no summary with a recommendation, but an information package: the questions the tutor asked, and points of attention that each refer back to the event they follow from. With that, they hold a different conversation than they would otherwise have held.

![](figures/fig-05-dossier.png)

**Figure 5.** (1) The screen is in its demo state here, and says so itself: it starts with recorded sample data and only loads real records once you act. So the data is an example. The rule beneath it is not. (2) "No grade, judgement or recommendation. This overview points the teacher at something; it does not judge. Every point above shows its source; a point without a valid source is refused by the tool itself." That is not a disclaimer bolted on afterwards: the server really does drop any point without a valid source reference, before the screen ever sees it. (3) Every suggested question carries a clickable reference back to the timeline event it came from. The teacher can always return to the evidence.

Two screens on, it is the same move: a point without a valid source never reaches the screen at all. You do not get a refusal like that in afterwards. By the time the screen exists and the demo is scheduled, nobody has a reason left to add it.

So the conversation does not get shorter, it gets sharper. And the time that does free up, I want to put where it makes a difference: into current material on top of the book. A case from last month, a figure from a sector that is moving right now.

When I started writing this piece, what stood here was that it could not be done. The wiki was deliberately read-only: the system read from it and never wrote to it. That was a requirement I had written down myself, and it was in my way.

So I revised it. Not by deleting the prohibition, but by writing down what must hold instead. Three question levels rather than six: understand, analyse, evaluate, with the reasons the other three drop out. Remember is answered by scrolling up the page. Apply needs a procedure this material does not supply. Create is what the checkpoint itself already demands. Further: the questions do not carry their level as a label, because the verb is supposed to give it away. Never a verdict. Never the answer. Always Dutch, even for an English-language video.

Then I pasted a YouTube link into a teacher's screen and ticked five chapters.

![](figures/fig-06-vragen.png)

**Figure 6.** (1) "Explain how..." Understand: can the student restate what the speaker is claiming? (2) "Compare... against the four perspectives in this chapter." Analyse: this is where the video meets the book. (3) "Assess to what extent..." Evaluate: make a judgement, and be able to say on what grounds. The levels are not labelled; the verb gives them away. Which is exactly what the instruction demanded.

That page now sits in the wiki, among the chapters it belongs to. You can see it in figure 1, at the bottom, the one card labelled video.

Two things are still missing, and both deliberately. The system writes the file but does not publish it: committing a change in another repository needs a key this service does not have, so a human presses the button. And the teacher picks the video. Nobody infers from a tutor conversation that something is absent. That is the next step, and it has not been taken.

But notice what did not happen. I did not talk the agent round. I found no phrasing that got past the prohibition. I revised one criterion and wrote down what replaces it, and then it built the thing. That is the same property that made it refuse me first.

That is the loop I want. The material gets richer, the gate is better informed, the assessment conversation gains depth, and that in turn produces hints about what material is missing. An hour you get back and put into the next round is a different thing from an hour you get back.

So if your programme runs another AI pilot next year, ask one question before anything gets built. Which criteria are we handing over, and where are they written down? If the answer is "our lecturers know that", then the answer is "nowhere", and you already know what you will get back. Start with the book you have already prescribed, because someone there did the work we have spent twenty years walking around. The problem was never that the machine does not understand us. It is that we never wrote it down.
