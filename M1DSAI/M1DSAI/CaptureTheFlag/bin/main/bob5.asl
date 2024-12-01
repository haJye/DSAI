
!start.

+!start <- enter;
	!move.

/* if the agent has no target, it randomly choses one*/
+!move : (not randomTarget(_,_)) <-
				X = math.floor(math.random(20)+1);
				Y = math.floor(math.random(20)+1);
				+randomTarget(X,Y);
				.print("My target is ",X," ",Y);
				!!move.

+!move : randomTarget(X,Y) & myPos(MYX,MYY) & (X > MYX) <- !right.
+!move : randomTarget(X,Y) & myPos(MYX,MYY) & (Y > MYY) <- !down.
+!move : randomTarget(X,Y) & myPos(MYX,MYY) & (Y < MYY) <- !up.
+!move : randomTarget(X,Y) & myPos(MYX,MYY) & (X < MYX) <- !left.

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

