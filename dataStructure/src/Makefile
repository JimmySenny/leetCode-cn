include ../etc/Makefile

ALLDIRS = ${WORKDIR}/src/array \
		  ${WORKDIR}/src/string \
		  ${WORKDIR}/src/dpointer \
		  ${WORKDIR}/src/queue-stack \
		  ${WORKDIR}/src/link \
		  ${WORKDIR}/src/hash \
		  ${WORKDIR}/src/tst 

all:
	@for subdir in ${ALLDIRS}; \
	do \
		cd $$subdir;\
		echo "Makeing $$subdir"; \
		${MAKE} ${MAKEOPT} all; \
		echo " Done "; \
	done

clean:
	@for subdir in ${ALLDIRS}; \
	do \
		cd $$subdir;\
		echo "Cleaning $$subdir"; \
		${MAKE} ${MAKEOPT} clean; \
		echo " Done "; \
	done
