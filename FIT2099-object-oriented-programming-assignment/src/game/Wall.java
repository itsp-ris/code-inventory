package game;

import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Ground;

public class Wall extends Ground {
	
	/**
	 * Constructor.
	 */
	public Wall() {
		super('#');
	}
	
	/**
	 * Returns false to indicate that Actor cannot enter
	 * @param actor the incoming Actor
	 */
	@Override
	public boolean canActorEnter(Actor actor) {
		return false;
	}
	
	/**
	 * Returns true to indicate that objects cannot pass through
	 */
	@Override
	public boolean blocksThrownObjects() {
		return true;
	}
}
