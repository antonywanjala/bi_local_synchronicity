    if int(setter) == 1:
        multiprocessing.freeze_support()

        MAX_INTRA_CONCURRENCY = int(7)  # Max tasks per this specific device
        MAX_INTER_CONCURRENCY = int(7)
        # Initial Setup Prompts
        raw_input = '1'
        dev_id = ''.join(filter(str.isdigit, raw_input)) or "1"

        intra_semaphore = multiprocessing.Semaphore(MAX_INTRA_CONCURRENCY)

        # Automated Startup Purge
        print("Scrubbing Drive for orphaned locks...")
        try:
            temp_service = get_drive_service()
            purge_all_locks(temp_service, LOCK_FOLDER_ID)
            print("✅ Cleanup complete. All previous locks purged.")
        except Exception as e:
            print(f"⚠️ Cleanup failed (check network): {e}")

        print(f'{MAX_INTRA_CONCURRENCY=}')
        print(f'{MAX_INTER_CONCURRENCY=}')
        # Main Loop
        while True:
            print(f"\n=== System Initialized (Device {dev_id}) ===")
            print("1. Instruction Builder / Relay Mode")
            print("2. Start Multi-Device Monitor Mode")
            print("3. Exit")
            choice = '2'

            if choice == '1':
                instruction_builder(dev_id, choice, intra_semaphore)

            elif choice == '2':
                # Dynamic polling and lock wait prompts
                p_int_input = '120'
                p_interval = int(p_int_input)

                l_wait_input = '120'
                l_wait = int(l_wait_input)

                input_mode_id = '5'

                if int(input_mode_id) == int('1'):
                    MONITOR_FOLDER_ID = input("Enter MONITOR_FOLDER_ID: ")
                elif int(input_mode_id) == int('2'):
                    MONITOR_FOLDER_ID = "1DSvZIGaEkBm5hjwCNKCiKyC-EvmEOw_v"
                elif int(input_mode_id) == int('3'):
                    MONITOR_FOLDER_ID = generate_instruction_set()
                elif int(input_mode_id) == int('4'):
                    MONITOR_FOLDER_ID = generate_instruction_set_ELEMENT3()  # prelim *7
                elif int(input_mode_id) == int('5'):
                    MONITOR_FOLDER_ID = generate_instruction_set_DESIGNATION4()  # vg_prompt_formula *7
                print(f'{MONITOR_FOLDER_ID=}')
                monitor_mode(dev_id, intra_semaphore, p_int=p_interval, lock_wait=l_wait)

            elif choice == '3':
                print("System shutting down.")
                sys.exit()
    elif int(setter) == 2:
        multiprocessing.freeze_support()

        MAX_INTRA_CONCURRENCY = int(7)  # Max tasks per this specific device
        MAX_INTER_CONCURRENCY = int(7)
        # Initial Setup Prompts
        raw_input = '1'
        dev_id = ''.join(filter(str.isdigit, raw_input)) or "1"

        intra_semaphore = multiprocessing.Semaphore(MAX_INTRA_CONCURRENCY)

        # Automated Startup Purge
        print("Scrubbing Drive for orphaned locks...")
        try:
            temp_service = get_drive_service()
            purge_all_locks(temp_service, LOCK_FOLDER_ID)
            print("✅ Cleanup complete. All previous locks purged.")
        except Exception as e:
            print(f"⚠️ Cleanup failed (check network): {e}")

        print(f'{MAX_INTRA_CONCURRENCY=}')
        print(f'{MAX_INTER_CONCURRENCY=}')
        # Main Loop
        while True:
            print(f"\n=== System Initialized (Device {dev_id}) ===")
            print("1. Instruction Builder / Relay Mode")
            print("2. Start Multi-Device Monitor Mode")
            print("3. Exit")
            choice = '2'

            if choice == '1':
                instruction_builder(dev_id, choice, intra_semaphore)

            elif choice == '2':
                # Dynamic polling and lock wait prompts
                p_int_input = '120'
                p_interval = int(p_int_input)

                l_wait_input = '120'
                l_wait = int(l_wait_input)

                input_mode_id = '4'

                if int(input_mode_id) == int('1'):
                    MONITOR_FOLDER_ID = input("Enter MONITOR_FOLDER_ID: ")
                elif int(input_mode_id) == int('2'):
                    MONITOR_FOLDER_ID = "1DSvZIGaEkBm5hjwCNKCiKyC-EvmEOw_v"
                elif int(input_mode_id) == int('3'):
                    MONITOR_FOLDER_ID = generate_instruction_set()
                elif int(input_mode_id) == int('4'):
                    MONITOR_FOLDER_ID = generate_instruction_set_ELEMENT3()  # prelim *7
                elif int(input_mode_id) == int('5'):
                    MONITOR_FOLDER_ID = generate_instruction_set_DESIGNATION4()  # vg_prompt_formula *7
                print(f'{MONITOR_FOLDER_ID=}')
                monitor_mode(dev_id, intra_semaphore, p_int=p_interval, lock_wait=l_wait)

            elif choice == '3':
                print("System shutting down.")
                sys.exit()
    elif int(setter) == 3:
        multiprocessing.freeze_support()

        MAX_INTRA_CONCURRENCY = int(input("Enter max_intra_concurrency: "))   # Max tasks per this specific device
        MAX_INTER_CONCURRENCY = int(input("Enter max_inter_concurrency: ")) # M  # Max tasks across ALL devices globally

        # Initial Setup Prompts
        raw_input = input("What device are you currently on (ex. 1, 2, 3)? >? ").strip()
        dev_id = ''.join(filter(str.isdigit, raw_input)) or "1"

        intra_semaphore = multiprocessing.Semaphore(MAX_INTRA_CONCURRENCY)

        # Automated Startup Purge
        print("Scrubbing Drive for orphaned locks...")
        try:
            temp_service = get_drive_service()
            purge_all_locks(temp_service, LOCK_FOLDER_ID)
            print("✅ Cleanup complete. All previous locks purged.")
        except Exception as e:
            print(f"⚠️ Cleanup failed (check network): {e}")

        print(f'{MAX_INTRA_CONCURRENCY=}')
        print(f'{MAX_INTER_CONCURRENCY=}')
        # Main Loop
        while True:
            print(f"\n=== System Initialized (Device {dev_id}) ===")
            print("1. Instruction Builder / Relay Mode")
            print("2. Start Multi-Device Monitor Mode")
            print("3. Exit")
            choice = input("> >? ").strip()

            if choice == '1':
                instruction_builder(dev_id, choice, intra_semaphore)

            elif choice == '2':
                # Dynamic polling and lock wait prompts
                p_int_input = input("Enter poll interval (seconds to check for NEW instructions): >? ").strip()
                p_interval = int(p_int_input) if p_int_input else 6

                l_wait_input = input("Enter lock wait timer (seconds to wait between busy-lock retries): >? ").strip()
                l_wait = int(l_wait_input) if l_wait_input else 6

                input_mode_id = input("Enter 1) MONITOR_FOLDER_ID, 2) 1DSvZIGaEkBm5hjwCNKCiKyC-EvmEOw_v, or 3) generate_instruction_set(), 4) generate_instruction_set_ELEMENT3(), or 5) generate_instruction_set_DESIGNATION4") or int("2")

                if int(input_mode_id) == int('1'):
                    MONITOR_FOLDER_ID = input("Enter MONITOR_FOLDER_ID: ")
                elif int(input_mode_id) == int('2'):
                    MONITOR_FOLDER_ID = "1DSvZIGaEkBm5hjwCNKCiKyC-EvmEOw_v"
                elif int(input_mode_id) == int('3'):
                    MONITOR_FOLDER_ID = generate_instruction_set()
                elif int(input_mode_id) == int('4'):
                    MONITOR_FOLDER_ID = generate_instruction_set_ELEMENT3() #prelim *7
                elif int(input_mode_id) == int('5'):
                    MONITOR_FOLDER_ID = generate_instruction_set_DESIGNATION4() #vg_prompt_formula *7
                print(f'{MONITOR_FOLDER_ID=}')
                monitor_mode(dev_id, intra_semaphore, p_int=p_interval, lock_wait=l_wait)

            elif choice == '3':
                print("System shutting down.")
                sys.exit()
            multiprocessing.freeze_support()

            MAX_INTRA_CONCURRENCY = int(7)  # Max tasks per this specific device
            MAX_INTER_CONCURRENCY = int(7)
            # Initial Setup Prompts
            raw_input = '1'
            dev_id = ''.join(filter(str.isdigit, raw_input)) or "1"

            intra_semaphore = multiprocessing.Semaphore(MAX_INTRA_CONCURRENCY)

            # Automated Startup Purge
            print("Scrubbing Drive for orphaned locks...")
            try:
                temp_service = get_drive_service()
                purge_all_locks(temp_service, LOCK_FOLDER_ID)
                print("✅ Cleanup complete. All previous locks purged.")
            except Exception as e:
                print(f"⚠️ Cleanup failed (check network): {e}")

            print(f'{MAX_INTRA_CONCURRENCY=}')
            print(f'{MAX_INTER_CONCURRENCY=}')
            # Main Loop
            while True:
                print(f"\n=== System Initialized (Device {dev_id}) ===")
                print("1. Instruction Builder / Relay Mode")
                print("2. Start Multi-Device Monitor Mode")
                print("3. Exit")
                choice = '2'

                if choice == '1':
                    instruction_builder(dev_id, choice, intra_semaphore)

                elif choice == '2':
                    # Dynamic polling and lock wait prompts
                    p_int_input = '30'
                    p_interval = int(p_int_input)

                    l_wait_input = '30'
                    l_wait = int(l_wait_input)

                    input_mode_id = '4'

                    if int(input_mode_id) == int('1'):
                        MONITOR_FOLDER_ID = input("Enter MONITOR_FOLDER_ID: ")
                    elif int(input_mode_id) == int('2'):
                        MONITOR_FOLDER_ID = "1DSvZIGaEkBm5hjwCNKCiKyC-EvmEOw_v"
                    elif int(input_mode_id) == int('3'):
                        MONITOR_FOLDER_ID = generate_instruction_set()
                    elif int(input_mode_id) == int('4'):
                        MONITOR_FOLDER_ID = generate_instruction_set_ELEMENT3()  # prelim *7
                    elif int(input_mode_id) == int('5'):
                        MONITOR_FOLDER_ID = generate_instruction_set_DESIGNATION4()  # vg_prompt_formula *7
                    print(f'{MONITOR_FOLDER_ID=}')
                    monitor_mode(dev_id, intra_semaphore, p_int=p_interval, lock_wait=l_wait)

                elif choice == '3':
                    print("System shutting down.")
                    sys.exit()
    elif int(setter) == 4:
        email_address = "komi622gefe@post.wordpress.com"
        multiprocessing.freeze_support()

        MAX_INTRA_CONCURRENCY = int(7)  # Max tasks per this specific device
        MAX_INTER_CONCURRENCY = int(7)
        # Initial Setup Prompts
        raw_input = '1'
        dev_id = ''.join(filter(str.isdigit, raw_input)) or "1"

        intra_semaphore = multiprocessing.Semaphore(MAX_INTRA_CONCURRENCY)

        # Automated Startup Purge
        print("Scrubbing Drive for orphaned locks...")
        try:
            temp_service = get_drive_service()
            purge_all_locks(temp_service, LOCK_FOLDER_ID)
            print("✅ Cleanup complete. All previous locks purged.")
        except Exception as e:
            print(f"⚠️ Cleanup failed (check network): {e}")

        print(f'{MAX_INTRA_CONCURRENCY=}')
        print(f'{MAX_INTER_CONCURRENCY=}')
        # Main Loop
        while True:
            print(f"\n=== System Initialized (Device {dev_id}) ===")
            print("1. Instruction Builder / Relay Mode")
            print("2. Start Multi-Device Monitor Mode")
            print("3. Exit")
            choice = '2'

            if choice == '1':
                instruction_builder(dev_id, choice, intra_semaphore)

            elif choice == '2':
                # Dynamic polling and lock wait prompts
                p_int_input = '30'
                p_interval = int(p_int_input)

                l_wait_input = '30'
                l_wait = int(l_wait_input)

                input_mode_id = '6'

                if int(input_mode_id) == int('1'):
                    MONITOR_FOLDER_ID = input("Enter MONITOR_FOLDER_ID: ")
                elif int(input_mode_id) == int('2'):
                    MONITOR_FOLDER_ID = "1DSvZIGaEkBm5hjwCNKCiKyC-EvmEOw_v"
                elif int(input_mode_id) == int('3'):
                    MONITOR_FOLDER_ID = generate_instruction_set()
                elif int(input_mode_id) == int('4'):
                    MONITOR_FOLDER_ID = generate_instruction_set_ELEMENT3()  # prelim *7
                elif int(input_mode_id) == int('5'):
                    MONITOR_FOLDER_ID = generate_instruction_set_DESIGNATION4()  # vg_prompt_formula *7
                elif int(input_mode_id) == int('6'):
                    MONITOR_FOLDER_ID = generate_instruction_set_send_to_post_designation(email_address=email_address)  # upload to draft for vg_prompt_formula
                print(f'{MONITOR_FOLDER_ID=}')
                monitor_mode(dev_id, intra_semaphore, p_int=p_interval, lock_wait=l_wait)

            elif choice == '3':
                print("System shutting down.")
                sys.exit()
    elif int(setter) == 5: #input_mode_id==6 only sends, doesn't generate instruction_set
        email_address = "komi622gefe@post.wordpress.com"
        multiprocessing.freeze_support()

        MAX_INTRA_CONCURRENCY = int(7)  # Max tasks per this specific device
        MAX_INTER_CONCURRENCY = int(7)
        # Initial Setup Prompts
        raw_input = '1'
        dev_id = ''.join(filter(str.isdigit, raw_input)) or "1"

        intra_semaphore = multiprocessing.Semaphore(MAX_INTRA_CONCURRENCY)

        # Automated Startup Purge
        print("Scrubbing Drive for orphaned locks...")
        try:
            temp_service = get_drive_service()
            purge_all_locks(temp_service, LOCK_FOLDER_ID)
            print("✅ Cleanup complete. All previous locks purged.")
        except Exception as e:
            print(f"⚠️ Cleanup failed (check network): {e}")

        print(f'{MAX_INTRA_CONCURRENCY=}')
        print(f'{MAX_INTER_CONCURRENCY=}')
        # Main Loop
        while True:
            print(f"\n=== System Initialized (Device {dev_id}) ===")
            print("1. Instruction Builder / Relay Mode")
            print("2. Start Multi-Device Monitor Mode")
            print("3. Exit")
            choice = '2'

            if choice == '1':
                instruction_builder(dev_id, choice, intra_semaphore)

            elif choice == '2':
                # Dynamic polling and lock wait prompts
                p_int_input = '30'
                p_interval = int(p_int_input)

                l_wait_input = '30'
                l_wait = int(l_wait_input)

                input_mode_id = '6'

                if int(input_mode_id) == int('1'):
                    MONITOR_FOLDER_ID = input("Enter MONITOR_FOLDER_ID: ")
                elif int(input_mode_id) == int('2'):
                    MONITOR_FOLDER_ID = "1DSvZIGaEkBm5hjwCNKCiKyC-EvmEOw_v"
                elif int(input_mode_id) == int('3'):
                    MONITOR_FOLDER_ID = generate_instruction_set()
                elif int(input_mode_id) == int('4'):
                    MONITOR_FOLDER_ID = generate_instruction_set_ELEMENT3()  # prelim *7
                elif int(input_mode_id) == int('5'):
                    MONITOR_FOLDER_ID = generate_instruction_set_DESIGNATION4()  # vg_prompt_formula *7
                elif int(input_mode_id) == int('6'):
                    MONITOR_FOLDER_ID = send_email_to_wordpress_vg_standard(email_address)  # upload to draft for vg_prompt_formula

                print(f'{MONITOR_FOLDER_ID=}')
                monitor_mode(dev_id, intra_semaphore, p_int=p_interval, lock_wait=l_wait)

            elif choice == '3':
                print("System shutting down.")
                sys.exit()
    
