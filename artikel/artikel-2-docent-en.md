# Do not give teachers time back, give them a better conversation

*Part 2 of two. [Part 1](artikel-1-criteria-en.md) was about what a programme has to write down before AI can build anything worthwhile. This part is about what it returns to the teacher.*

The pitch for AI in education is almost always time saved. Marking goes faster, making tests goes faster, feedback comes back sooner.

That is the weakest version of the argument, and a room of teachers rightly distrusts it. Because time saved on marking does not make the final conversation with a student one millimetre better. You arrive at the table with the same questions as last year, only earlier in the day. And teachers sense exactly what sits underneath that promise: if the work is routine enough for a machine to take over, how long before somebody asks whether the teacher is still needed.

So what should AI actually return?

Something you could not have done without it. Not the same conversation, faster, but a different conversation: with questions you would not otherwise have asked, because you did not know they were there. The return should be cognitive, not administrative.

The screens below come from a module I rebuilt this year. Students work in teams, submit a checkpoint each phase, and that work passes two gates before the next phase unlocks: a Socratic AI tutor and a peer partner team. What the teacher sees of all that is what this piece is about. Three things, and they stand independently.

## The teacher keeps the last word, and has to justify it

The first question any teacher asks about an AI gate: who actually decides?

![](figures/fig-04-dashboard.png)

**Figure 4.** (1) This screen is in its demo state too, and says so itself. What sits underneath is built: the route exists, and against a real class it returns real figures. (2) "Hidden score": the grade the student never sees and the teacher does. Not because it worked out that way, but because the team-facing report structurally has no field a score could go in. (3) The teacher can overrule the AI's gate. The server records every override in an audit trail, and refuses one that carries no stated reason: an override nobody can explain later is exactly what a student would ask about.

The teacher decides. They can open a gate the tutor held shut. But not quietly, and not without a reason.

That an override requires a written justification is not a tidy afterthought. It is in the requirements, so the server refuses one without it. And here it gets interesting: the button above it cannot currently even reach that server, because of a fault in the wiring. The rule therefore holds before the function works. You only get that order of events if somebody wrote it down first; build it the other way round and by the time the screen exists, nobody has a reason left to add the refusal.

Note the second marker too. The grade does exist, and the teacher sees it, but the team does not. That is not a setting someone left switched on by accident: the report that goes to the team simply has no field a score could sit in. A grade cannot end up there, not even if a model wanted to put it there.

## The teacher gets evidence, not a verdict

For the final assessment you would expect a summary with a recommendation. "This team is weak on process analysis, watch for that." That is precisely what this system does not deliver.

![](figures/fig-05-dossier.png)

**Figure 5.** (1) The screen is in its demo state here, and says so itself: it starts with recorded sample data and only loads real records once you act. So the data is an example. The rule beneath it is not. (2) "No grade, judgement or recommendation. This overview points the teacher at something; it does not judge. Every point above shows its source; a point without a valid source is refused by the tool itself." That is not a disclaimer bolted on afterwards: the server really does drop any point without a valid source reference, before the screen ever sees it. (3) Every suggested question carries a clickable reference back to the timeline event it came from. The teacher can always return to the evidence.

What the teacher gets is an information package: the questions the tutor asked, and points of attention that each refer back to the event they follow from. They can always click through to the moment itself.

That difference is bigger than it looks. A summary with a verdict takes over the thinking and produces a teacher who turns up to confirm a model's judgement. A package with sources does the opposite: it points you at things you would not have found again yourself, and leaves the conclusion where it belongs. The conversation does not get shorter. It gets sharper.

And there it is again, that refusal: a point without a valid source never reaches the screen. The same move as the override, on a completely different component, for the same reason.

## The time that frees up goes back into the material

The third return is the only one that resembles time saved, and it works only if you spend that time on something.

For me, on current material on top of the book: a case from last month, a figure from a sector that is moving right now. When I started on this module that was impossible. The wiki was deliberately read-only, the system read from it and never wrote to it. That was a requirement I had written down myself, and it was in my way.

So I revised it. Not by deleting the prohibition, but by writing down what must hold instead. Three question levels rather than six: understand, analyse, evaluate, with the reasons the other three drop out. Remember is answered by scrolling up the page. Apply needs a procedure this material does not supply. Create is what the checkpoint itself already demands. Further: the questions do not carry their level as a label, because the verb is supposed to give it away. Never a verdict. Never the answer. Always Dutch, even for an English-language video.

Then I pasted a YouTube link into a teacher's screen and ticked five chapters.

![](figures/fig-06-vragen.png)

**Figure 6.** (1) "Explain how..." Understand: can the student restate what the speaker is claiming? (2) "Compare... against the four perspectives in this chapter." Analyse: this is where the video meets the book. (3) "Assess to what extent..." Evaluate: make a judgement, and be able to say on what grounds. The levels are not labelled; the verb gives them away. Which is exactly what the instruction demanded.

That page now sits in the wiki, among the chapters it belongs to.

Two things are still missing, and both deliberately. The system writes the file but does not publish it: committing a change in another repository needs a key this service does not have, so a human presses the button. And the teacher picks the video. Nobody infers from a tutor conversation that something is absent. That is the next step, and it has not been taken.

But notice what did not happen. I did not talk the agent round. I found no phrasing that got past the prohibition. I revised one criterion and wrote down what replaces it, and then it built the thing. That is the same property that made it refuse me first.

## What a teacher is left with

Three things, none of them about time. They still decide, but have to be able to explain their departure. They get evidence instead of a verdict, and walk into the final conversation with questions they would not have found themselves. And the material they add comes back to the student, in the place the book says it belongs.

That is a different promise from time saved, and an honester one. An hour you get back and immediately spend again is not a gain. A conversation in which you ask a question you could not have asked last year, that is one.
