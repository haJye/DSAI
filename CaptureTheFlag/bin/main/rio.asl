
!start.

+!start <- enter;
	!move.

/* if the agent sees a red flag, it informs every other agent of its position*/
+pos(X,Y,blueFlag): not target(_,_) <-
		       		     +target(X,Y);
				     .print("Let's attack ",X," ",Y);
		       		     .broadcast(tell,target(X,Y)).

/* if the agent has no target, it randomly choses one*/
+!move : (not randomTarget(_,_)) <-
				X = math.floor(math.random(20)+1);
				Y = math.floor(math.random(20)+1);
				+randomTarget(X,Y);
				.print("My target is ",X," ",Y);
				!!move.

/* if the agent has a new target, it drops any random target*/
+target(_,_)[source(self)] : randomTarget(X,Y) <- -randomTarget(X,Y);
						+leader;
						!attack.

+target(_,_)[source(A)] : randomTarget(X,Y) & (A \== self) <- -randomTarget(X,Y);
							.send(A,tell,inTeam);
							!attack.

/* once the agent is besides the target it unregisters from the team*/

+!attack : target(X,Y) & myPos (X-1,Y) <- .broadcast(untell,inTeam).
+!attack : target(X,Y) & myPos (X+1,Y) <- .broadcast(untell,inTeam).
+!attack : target(X,Y) & myPos (X,Y-1) <- .broadcast(untell,inTeam).
+!attack : target(X,Y) & myPos (X,Y+1) <- .broadcast(untell,inTeam).
+!attack : target(X,Y) & myPos (X-1,Y-1) <- .broadcast(untell,inTeam).
+!attack : target(X,Y) & myPos (X-1,Y+1) <- .broadcast(untell,inTeam).
+!attack : target(X,Y) & myPos (X+1,Y-1) <- .broadcast(untell,inTeam).
+!attack : target(X,Y) & myPos (X+1,Y+1) <- .broadcast(untell,inTeam).

/* if every agent have unregistered the target is forgotten and the leader asks them to start again moving.*/
-inTeam : not inTeam & leader & target(X,Y) <- .print("Flag reached. Let's move again ! !");
					-leader;
					-target(X,Y);
					.broadcast(untell,target(X,Y));
					.broadcast(achieve,move);
					!move.

/* Plans to attack a target */								
+!attack : target(X,Y) & myPos(MYX,MYY) & (X > MYX) <- !right.
+!attack : target(X,Y) & myPos(MYX,MYY) & (Y > MYY) <- !down.
+!attack : target(X,Y) & myPos(MYX,MYY) & (Y < MYY) <- !up.
+!attack : target(X,Y) & myPos (MYX,MYY) & (X < MYX) <- !left.

+myPos(MYX,MYY): target(X,Y) <- !attack.

/* Plans to move towards a random target */

+!move : randomTarget(X,Y) & myPos(MYX,MYY) & (X > MYX) <- !right.
+!move : randomTarget(X,Y) & myPos(MYX,MYY) & (Y > MYY) <- !down.
+!move : randomTarget(X,Y) & myPos(MYX,MYY) & (Y < MYY) <- !up.
+!move : randomTarget(X,Y) & myPos (MYX,MYY) & (X < MYX) <- !left.

+!left : myPos(MYX,MYY) & pos(MYX-1,MYY,empty) <- left.
+!left : myPos(MYX,MYY) & (not pos(MYX-1,MYY,empty)) <- !down.
+!up : myPos(MYX,MYY) & pos(MYX,MYY-1,empty) <- up;.
+!up : myPos(MYX,MYY) & (not pos(MYX,MYY-1,empty)) <- !right.
+!right : myPos(MYX,MYY) & pos(MYX+1,MYY,empty) <- right.
+!right : myPos(MYX,MYY) & (not pos(MYX+1,MYY,empty)) <- !down.
+!down : myPos(MYX,MYY) & pos(MYX,MYY+1,empty) <- down.
+!down : myPos(MYX,MYY) & (not pos(MYX,MYY+1,empty)) <- !right.

+myPos(MYX,MYY): randomTarget(MYX,MYY) <- -randomTarget(MYX,MYY);!move.
+myPos(MYX,MYY): randomTarget(X,Y) <- !move.



+team(red).
