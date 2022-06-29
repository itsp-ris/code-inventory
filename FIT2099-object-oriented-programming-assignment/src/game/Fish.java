package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.DoNothingAction;
import edu.monash.fit2099.engine.GameMap;

public class Fish extends Actor {
	private Behaviour wanderBehaviour;
	int age;
	
	public Fish(String name, char displayChar, int age) {
		super(name, displayChar, 5);
		wanderBehaviour = new WanderBehaviour();
		this.age = age;
		ActorSpecies.PLESIOSAURS.addTarget(this);
		ActorSpecies.PTERANODONS.addTarget(this);
	}
	
	/**
	 * Returns a collection of the Actions that the otherActor can do to the current Actor.
	 *
	 * @param otherActor the Actor that might be performing attack
	 * @param direction  String representing the direction of the other Actor
	 * @param map        current GameMap
	 * @return A collection of Actions.
	 */
	@Override
	public Actions getAllowableActions(Actor otherActor, String direction, GameMap map) {
		if (otherActor.getActorClass() != ActorClass.HERBIVORE && otherActor.getActorEco() != ActorClass.LANDBASED) {
			Actions actions = new Actions();
			actions.add(new AttackAction(this));
			return actions;
		}
		return super.getAllowableActions(otherActor, direction, map);
	}
	

	/**
	 * Select and return an action to perform on the current turn. 
	 *
	 * @param actions    Collection of possible Actions for this Actor
	 * @param lastAction The Action this Actor took last turn. Can do interesting things in conjunction with Action.getNextAction()
	 * @param map        The map containing the Actor
	 * @param display    The I/O object to which messages may be written
	 * @return the Action to be performed
	 */
	@Override
	public Action playTurn(Actions actions, Action lastAction, GameMap map, Display display) {
		age += 1;
		
		Action wander = wanderBehaviour.getAction(this, map);
		if (wander != null) {
			return wander;
		}
		
		return new DoNothingAction();
	}
	
	/**
	 * Accessor for the Dinosaur's species.
	 * @return the Dinosaur's species
	 */
	@Override
	public ActorSpecies getSpecies() {
		return ActorSpecies.FISH;
	}
	
	/**
	 * Accessor for the Dinosaur's category.
	 * @return the Dinosaur's category
	 */
	@Override
	public ActorClass getActorClass() {
		return null;
	}
	
	/**
	 * Accessor for the Dinosaur's habitat category.
	 * @return the Dinosaur's habitat category
	 */
	@Override
	public ActorClass getActorEco() {
		return ActorClass.WATERBASED;
	}
}
