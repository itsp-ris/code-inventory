package game;

import java.util.Random;

import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Exit;
import edu.monash.fit2099.engine.Ground;
import edu.monash.fit2099.engine.Location;

public class Water extends Ground {
	private Random rand = new Random();

	public Water() {
		super('~');
	}
	
	/**
	 * Inform the passage of time.
	 * @param location The location of the Ground 
	 */
	@Override
	public void tick(Location location) {
		super.tick(location);
		
		growReed(location);
	}
	
	/**
	 * Set the current Ground to Grass.
	 * @param location the position of the Ground
	 * @return boolean
	 */
	private boolean growReed(Location location) {
		boolean groundAdjacent = false;
		boolean reedAdjacent = false;
		for (Exit exit : location.getExits()) {
			Location adjacent = exit.getDestination();
			
			if (adjacent.getGround() instanceof Dirt) {
				groundAdjacent = true;
			}
		}
		
		for (Exit exit : location.getExits()) {
			Location adjacent = exit.getDestination();
			
			if (adjacent.getGround() instanceof Reed && !groundAdjacent) {
				reedAdjacent = true;
			}
		}
		
		if (rand.nextDouble() <= 0.1 && groundAdjacent) {
			location.setGround(new Reed());
			return true;
		}
		
		if (rand.nextDouble() <= 0.05 && !groundAdjacent && reedAdjacent) {
			location.setGround(new Reed());
			return true;
		}
		
		return false;
	}
	
	/**
	 * Control type of actor entering terrain
	 * @param actor the actor that wants to enter this terrain
	 * @return boolean
	 */
	public boolean canActorEnter(Actor actor) {
		if (actor.getActorEco() != ActorClass.LANDBASED) { 
			return true;
		}
		return false;
	}
}
