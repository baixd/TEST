void fmc_write_32bit_data(uint32_t address, uint16_t length, int32_t* data_32)
{
    uint16_t StartSector, EndSector,i;
    /* unlock the flash program erase controller */
    fmc_unlock();
    /* clear pending flags */
    fmc_flag_clear(FMC_FLAG_END | FMC_FLAG_OPERR | FMC_FLAG_WPERR | FMC_FLAG_PGMERR | FMC_FLAG_PGSERR);
	
		if(frist_flag == 0){
			frist_flag = 1;
			/* get the number of the start and end sectors */
			StartSector = fmc_sector_get(address);
			EndSector = fmc_sector_get(address + 4*length);
			/* each time the sector number increased by 8, refer to the sector definition */
			for(i = StartSector; i <= EndSector; i += 8){
					if(FMC_READY != fmc_sector_erase(i)){
							while(1);
					}
			}
		}
    /* write data_32 to the corresponding address */
    for(i=0; i<length; i++){
        if(FMC_READY == fmc_word_program(address, data_32[i])){
            address = address + 4;
        }else{ 
            while(1);
        }
    }
    /* lock the flash program erase controller */
    fmc_lock();
}