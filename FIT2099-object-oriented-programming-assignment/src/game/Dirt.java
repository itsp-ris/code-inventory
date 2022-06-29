package game;

import java.util.Random;

import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Exit;
import edu.monash.fit2099.engine.Ground;
import edu.monash.fit2099.engine.Location;

/**
 * A class that represents bare dirt.
 */
public class Dirt extends Ground {
	private Random rand = new Random();
	
	public Dirt() {
		super('.');
	}
	
	/**
	 * Inform the passage of time.
	 * @param location The location of the Ground 
	 */
	@Override
	public void tick(Location location) {
		super.tick(location);
		
		if (!growGrass(location)) {
			growTree(location);
		}
	}
	
	/**
	 * Set the current Ground to Grass.
	 * @param location the position of the Ground
	 * @return boolean
	 */
	private boolean growGrass(Location location) {
		if (rand.nextDouble() <= 0.005 && !location.containsAnActor()) {
			location.setGround(new Grass());
			ActorClass.HERBIVORE.addFoodSource(location);
			return true;
		}
		
		return false;
	}
	
	/**
	 * Set the current Ground to Tree.
	 * @param location the position of the Ground
	 * @return boolean
	 */
	private boolean growTree(Location location) {
		for (Exit exit : location.getExits()) {
			Location adjacent = exit.getDestination();
			
			if (adjacent.getGround() instanceof Tree) {
				if (rand.nextDouble() <= 0.005 && !location.containsAnActor()) {
					location.setGround(new Tree());
					ActorClass.HERBIVORE.addFoodSource(location);
					return true;
				}
			}
		}
		
		return false;
	}
	
	/**
	 * Control type of actor entering terrain
	 * @param actor the actor that wants to enter this terrain
	 * @return boolean
	 */
	public boolean canActorEnter(Actor actor) {
		if (actor.getActorEco() != ActorClass.WATERBASED) { 
			return true;
		}
		return false;
	}
}
