package game;

import edu.monash.fit2099.demo.conwayslife.Status;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Ground;
import edu.monash.fit2099.engine.Location;
import edu.monash.fit2099.interfaces.FoodInterface;

public class Tree extends Ground implements FoodInterface {
	private int age = 0;
	private int nutrients = 10;
	private Status status = Status.ONGROUND;

	public Tree() {
		super('+');
	}
	
	/**
	 * Inform the passage of time.
	 * @param location The location of the Ground 
	 */
	@Override
	public void tick(Location location) {
		super.tick(location);
		
		if (status == Status.EATEN) {
			location.setGround(new Dirt());
		} else {
			age++;
			if (age == 10)
				displayChar = 't';
			if (age == 20)
				displayChar = 'T';
		}
	}
	
	/**
	 * Returns a list of Actions allowed to perform on the Ground.
	 *
	 * @param actor the Actor acting
	 * @param location the current Location
	 * @param direction the direction of the Ground from the Actor
	 * @return a new, empty collection of Actions
	 */
	@Override
	public Actions allowableActions(Actor actor, Location location, String direction) {
		if (actor.getActorClass() == ActorClass.HERBIVORE) {
			Actions actions = new Actions();
			actions.add(new FeedAction(this));
			return actions;
		}
		
		return super.allowableActions(actor, location, direction);
	}
	
	/**
	 * Accessor for the Ground's nutrients when consumed.
	 * @return the Ground's nutrients
	 */
	@Override
	public int getNutrients() {
		return nutrients;
	}

	/**
	 * Modifies the current condition of the Ground.
	 * @param newStatus the status to replace the current status
	 */
	@Override
	public void setStatus(Status newStatus) {
		status = newStatus;
	}
}
