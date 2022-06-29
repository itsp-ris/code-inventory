package edu.monash.fit2099.interfaces;

import game.ActorClass;
import game.ActorSpecies;

/**
 * This interface provides the ability to add methods to Actor, without modifying code in the engine,
 * or downcasting references in the game.   
 */

public interface ActorInterface {
	
	/**
	 * Accessor for the Actor's species.
	 * @return the Actor's species
	 */
	public ActorSpecies getSpecies();
	
	/**
	 * Accessor for the Actor's class.
	 * @return the Actor's class
	 */
	public ActorClass getActorClass();

	/**
	 * Accessor for the Actor's eco.
	 * @return the Actor's eco
	 */
	public ActorClass getActorEco();
}
