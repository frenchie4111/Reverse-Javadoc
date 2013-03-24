class java.lang.Object
  CarRadio {

	static int MAX_VOLUME
	static int MIN_VOLUME


	/**
	 * Toggle the frequency band of the car radio.
	 * 
	 * 
	 * When changing from AM band to FM band, the car radio returns to
	 * the last frequency tuned while in the FM band.  Similarly, when
	 * changing from FM band to AM band, the car radio returns to the
	 * last frequency tuned while in the AM band.
	 * 
	 * 
	 * The factory default setting for the frequency band is the AM band.
	 */
	public void amfmBtn() {
		//Body
	}

	/**
	 * Return the car radio display.
	 * 
	 * 
	 * Returns:A sequence of four strings depicting the current car radio state.
	 * 
	 * Examples:
	 * 
	 * ---------------------
	 * |                   |
	 * |                   |
	 * ---------------------
	 * 
	 * 
	 * ---------------------
	 * |  AM   1610  ****  |
	 * |  Vol: --          |
	 * ---------------------
	 * 
	 * 
	 * ---------------------
	 * |  FM   91.5  WXXI  |
	 * |  Vol: 10    SET1  |
	 * ---------------------
	 * 
	 * 
	 * 
	 * The format of the display is as follows:
	 * 
	 * If the power is off, then:
	 * 
	 * Line 1: A string of 21 '-' characters.
	 * Lines 2 and 3: A string of 21 characters, comprised of
	 * a '|' character, 19 spaces, and a '|'
	 * character.
	 * Line 4: A string of 21 '-' characters.
	 * 
	 * If the power is on, then:
	 * 
	 * Line 1: A string of 21 '-' characters.
	 * Line 2: A string of 21 characters, comprised of a
	 * '|' character, two spaces, either the string
	 * "AM" or the string "FM" (reflecting the current
	 * frequency band), sufficient spaces to right justify the current
	 * frequency in column 12, the tuned frequency, two spaces, the
	 * station id if tuned to a viable station or the string
	 * "****" if not tuned to a viable station, two spaces,
	 * and a '|' character.
	 * Line 3: A string of 21 characters, comprised of a
	 * '|' character, two spaces, the string "Vol:",
	 * sufficient spaces to right justify the current volume in column
	 * 10, the current volume if not muted and the string "--"
	 * if muted, four spaces, either four spaces if the
	 * radio is unprepared to set a preset frequency or the string
	 * "SET1" if the radio is prepared to set a primary preset
	 * frequency or thes string "SET2" if the radio is
	 * prepared to set a secondary preset frequency, two spaces, and a
	 * '|' character.
	 * Line 4: A string of 21 '-' characters.
	 */
	public java.util.ArrayList<java.lang.String> display() {
		//Body
	}

	/**
	 * Toggles the mute status of the car radio.
	 * 
	 * 
	 * When the car radio is muted, the volume may be changed, but the
	 * car radio remains muted.
	 * 
	 * 
	 * The factory default setting for the mute status is unmuted.
	 */
	public void muteBtn() {
		//Body
	}

	/**
	 * Turns the car radio on and off.
	 * 
	 * 
	 * When the car radio is off, it retains, but buttons do not
	 * change, the state of the volume (and mute), am/fm band and
	 * frequency, and presets.
	 */
	public void powerBtn() {
		//Body
	}

	/**
	 * Tune to or set preset #1.
	 * 
	 * 
	 * There are primary and secondary preset #1 frequencies for both
	 * the AM band and the FM band.
	 * 
	 * 
	 * If the radio is unprepared to set a preset frequency:
	 * If the car radio is not tuned to the primary preset #1
	 * frequency (for the current frequency band), then tune to the
	 * primary preset #1 frequency (for the current frequency band).
	 * Otherwise (if the car radio is already tuned to the primary
	 * preset #1 frequency (for the current frequency band)), then
	 * tune to the secondary preset #1 frequency (for the current
	 * frequency band).
	 * 
	 * 
	 * If the radio is prepared to set a primary preset frequency:
	 * Set the primary preset #1 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * If the radio is prepared to set a secondary preset frequency:
	 * Set the secondary preset #1 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * The factory default settings for the primary and secondary
	 * preset #1 frequencies for the AM band are the minimum AM band
	 * frequency (520kHz).  The factory default settings for the
	 * primary and secondary preset #1 frequencies for the FM band are
	 * the minimum FM band frequency (87.9MHz).
	 */
	public void preset1Btn() {
		//Body
	}

	/**
	 * Tune to or set preset #2.
	 * 
	 * 
	 * There are primary and secondary preset #2 frequencies for both
	 * the AM band and the FM band.
	 * 
	 * 
	 * If the radio is unprepared to set a preset frequency:
	 * If the car radio is not tuned to the primary preset #2
	 * frequency (for the current frequency band), then tune to the
	 * primary preset #2 frequency (for the current frequency band).
	 * Otherwise (if the car radio is already tuned to the primary
	 * preset #2 frequency (for the current frequency band)), then
	 * tune to the secondary preset #2 frequency (for the current
	 * frequency band).
	 * 
	 * 
	 * If the radio is prepared to set a primary preset frequency:
	 * Set the primary preset #2 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * If the radio is prepared to set a secondary preset frequency:
	 * Set the secondary preset #2 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * The factory default settings for the primary and secondary
	 * preset #2 frequencies for the AM band are the minimum AM band
	 * frequency (520kHz).  The factory default settings for the
	 * primary and secondary preset #2 frequencies for the FM band are
	 * the minimum FM band frequency (87.9MHz).
	 */
	public void preset2Btn() {
		//Body
	}

	/**
	 * Tune to or set preset #3.
	 * 
	 * 
	 * There are primary and secondary preset #3 frequencies for both
	 * the AM band and the FM band.
	 * 
	 * 
	 * If the radio is unprepared to set a preset frequency:
	 * If the car radio is not tuned to the primary preset #3
	 * frequency (for the current frequency band), then tune to the
	 * primary preset #3 frequency (for the current frequency band).
	 * Otherwise (if the car radio is already tuned to the primary
	 * preset #3 frequency (for the current frequency band)), then
	 * tune to the secondary preset #3 frequency (for the current
	 * frequency band).
	 * 
	 * 
	 * If the radio is prepared to set a primary preset frequency:
	 * Set the primary preset #3 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * If the radio is prepared to set a secondary preset frequency:
	 * Set the secondary preset #3 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * The factory default settings for the primary and secondary
	 * preset #3 frequencies for the AM band are the minimum AM band
	 * frequency (520kHz).  The factory default settings for the
	 * primary and secondary preset #3 frequencies for the FM band are
	 * the minimum FM band frequency (87.9MHz).
	 */
	public void preset3Btn() {
		//Body
	}

	/**
	 * Tune to or set preset #4.
	 * 
	 * 
	 * There are primary and secondary preset #4 frequencies for both
	 * the AM band and the FM band.
	 * 
	 * 
	 * If the radio is unprepared to set a preset frequency:
	 * If the car radio is not tuned to the primary preset #4
	 * frequency (for the current frequency band), then tune to the
	 * primary preset #4 frequency (for the current frequency band).
	 * Otherwise (if the car radio is already tuned to the primary
	 * preset #4 frequency (for the current frequency band)), then
	 * tune to the secondary preset #4 frequency (for the current
	 * frequency band).
	 * 
	 * 
	 * If the radio is prepared to set a primary preset frequency:
	 * Set the primary preset #4 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * If the radio is prepared to set a secondary preset frequency:
	 * Set the secondary preset #4 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * The factory default settings for the primary and secondary
	 * preset #4 frequencies for the AM band are the minimum AM band
	 * frequency (520kHz).  The factory default settings for the
	 * primary and secondary preset #4 frequencies for the FM band are
	 * the minimum FM band frequency (87.9MHz).
	 */
	public void preset4Btn() {
		//Body
	}

	/**
	 * Tune to or set preset #5.
	 * 
	 * 
	 * There are primary and secondary preset #5 frequencies for both
	 * the AM band and the FM band.
	 * 
	 * 
	 * If the radio is unprepared to set a preset frequency:
	 * If the car radio is not tuned to the primary preset #5
	 * frequency (for the current frequency band), then tune to the
	 * primary preset #5 frequency (for the current frequency band).
	 * Otherwise (if the car radio is already tuned to the primary
	 * preset #5 frequency (for the current frequency band)), then
	 * tune to the secondary preset #5 frequency (for the current
	 * frequency band).
	 * 
	 * 
	 * If the radio is prepared to set a primary preset frequency:
	 * Set the primary preset #5 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * If the radio is prepared to set a secondary preset frequency:
	 * Set the secondary preset #5 frequency (for the current
	 * frequency band) to the tuned frequency.
	 * 
	 * 
	 * The factory default settings for the primary and secondary
	 * preset #5 frequencies for the AM band are the minimum AM band
	 * frequency (520kHz).  The factory default settings for the
	 * primary and secondary preset #5 frequencies for the FM band are
	 * the minimum FM band frequency (87.9MHz).
	 */
	public void preset5Btn() {
		//Body
	}

	/**
	 * Decreases the tuned frequency until a viable station is tuned.
	 * 
	 * 
	 * Seeks through decreasing frequencies (and "wrapping" to the
	 * maximum frequency after seeking past the minimum fequency for
	 * the current frequency band) for a viable station.  A station is
	 * viable if the StationData object with which
	 * the car radio was constructed returns a non-null
	 * String from the
	 * lookupFreq method.
	 * 
	 * 
	 * If no viable stations are found after seeking through all
	 * frequencies, then the car radio remains tuned to the original
	 * frequency.
	 */
	public void seekDownBtn() {
		//Body
	}

	/**
	 * Increases the tuned frequency until a viable station is tuned.
	 * 
	 * 
	 * Seeks through increasing frequencies (and "wrapping" to the
	 * minimum frequency after seeking past the maximum fequency for
	 * the current frequency band) for a viable station.  A station is
	 * viable if the StationData object with which
	 * the car radio was constructed returns a non-null
	 * String from the
	 * lookupFreq method.
	 * 
	 * 
	 * If no viable stations are found after seeking through all
	 * frequencies, then the car radio remains tuned to the original
	 * frequency.
	 */
	public void seekUpBtn() {
		//Body
	}

	/**
	 * Prepare to set a primary or secondary preset frequency.
	 * 
	 * 
	 * If the radio is unprepared to set a preset frequency:
	 * Prepare the radio to set a primary preset frequency.
	 * 
	 * 
	 * If the radio is prepared to set a primary preset frequency:
	 * Prepare the radio to set a secondary preset frequency.
	 * 
	 * 
	 * If the radio is prepared to set a secondary preset frequency:
	 * Unprepare the radio to set a preset frequency.
	 * 
	 * 
	 * The factory default setting is unprepared to set a preset frequency.
	 * 
	 * 
	 * After powering the radio on or off, toggling the frequency
	 * band, changing the tuned frequency (either through tuning or
	 * seeking), or setting a primary or secondary preset, the radio
	 * is unprepared to set a preset frequency.
	 */
	public void setBtn() {
		//Body
	}

	/**
	 * Decreases the tuned frequency by one unit.
	 * 
	 * 
	 * While in the AM band, the frequency is decreased by 10kHz.  The
	 * minimum AM band frequency is 520kHz; decreasing the frequency
	 * beyond the minimum frequency "wraps" to the maximum frequency
	 * (1610kHz).
	 * 
	 * 
	 * While in the FM band, the frequency is decreased by 200kHz.
	 * The minimum FM band frequency is 87.9MHz; decreasing the
	 * frequency beyond the minimum frequency "wraps" to the maximum
	 * frequency (107.9MHz).
	 */
	public void tuneDownBtn() {
		//Body
	}

	/**
	 * Increases the tuned frequency by one unit.
	 * 
	 * 
	 * While in the AM band, the frequency is increased by 10kHz.  The
	 * maximum AM band frequency is 1610kHz; increasing the frequency
	 * beyond the maximum frequency "wraps" to the minimum frequency
	 * (520kHz).
	 * 
	 * 
	 * While in the FM band, the frequency is increased by 200kHz.
	 * The maximum FM band frequency is 107.9MHz; increasing the
	 * frequency beyond the maximum fequency "wraps" to the minimum
	 * frquency (87.9MHz).
	 * 
	 * 
	 * The factory default setting for the frequency when in the AM
	 * band is the minimum frequency (520kHz).  The factory default
	 * setting for the frequency when in the FM band is the minimum
	 * frequency (87.9MHz).
	 */
	public void tuneUpBtn() {
		//Body
	}

	/**
	 * Decreases the car radio volume by one unit.
	 * 
	 * 
	 * The car radio has a minimum volume of 0; attempts to decrease
	 * the volume beyond the minimum volume should not change the
	 * volume.
	 * 
	 * 
	 * The factory default setting for the volume is 0.
	 */
	public void volumeDownBtn() {
		//Body
	}

	/**
	 * Increases the car radio volume by one unit.
	 * 
	 * 
	 * The car radio has a maximum volume of 20; attempts to increase
	 * the volume beyond the maximum volume should not change the
	 * volume.
	 * 
	 * 
	 * The factory default setting for the volume is 0.
	 */
	public void volumeUpBtn() {
		//Body
	}


}
