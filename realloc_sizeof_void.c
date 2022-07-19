int  main () {
		
		int *ptr;
		
		ptr = (int*) malloc (5*sizeof(int));
		
		ptr = (int*) realloc (ptr,22*sizeof(int));

		
		void  free (void*ptr);
		
		return  0;
	}
