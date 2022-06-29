package game;

import java.util.Random;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.GameMap;

/**
 * Class representing a Dinosaur's characteristic
 */
public class ReproduceBehaviour implements Behaviour {
	private Random rand = new Random();
	
	/**
	 * Returns a LayEggsAction to reproduce.  
	 * If no reproduction is possible, returns null.
	 * 
	 * @param actor The Dinosaur enacting the behaviour
	 * @param map 	The map that Dinosaur is currently on
	 * @return an Action, or null if no LayEggsAction is possible
	 */
	@Override
	public Action getAction(Actor actor, GameMap map) {
		//Dinosaur has 50% chance to lay eggs.
		if (rand.nextBoolean()) {
			return new LayEggsAction();
		}
		
		return null;
	}

}
