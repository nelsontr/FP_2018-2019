#!/bin/bash

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "1 (all students) directory required, $# provided"

indir=$1

pwd=`pwd`
outdir=$pwd/output
bindir=$pwd/bin

rm -rf $outdir

################# Functions #######################
function process_student {
	student=$1
	stindir=$indir/$student/
	stoutdir=$outdir/$student/

	mkdir -p $stoutdir

	pythonfile=`ls $stindir/*.py`

	## TESTES_tabuleiro
	funtest=$bindir/TESTES_tabuleiro.py
	fun=`basename $funtest .py`
	#### Mudando TAD celula
	cat $pythonfile $bindir/TAD_celula.py $funtest > $stoutdir/${fun}_celula.py
	#### Mudando TAD coordenada
	cat $pythonfile $bindir/TAD_coordenada.py $funtest > $stoutdir/${fun}_coordenada.py
	#### Mudando TAD celula e coordenada
	cat $pythonfile $bindir/TAD_celula.py $bindir/TAD_coordenada.py $funtest > $stoutdir/${fun}_celula_coordenada.py

	for py in $stoutdir/${fun}_*.py; do
	    echo "python3 $py"
	    python3 $py
	done

	## TESTES_portas
	funtest=$bindir/TESTES_portas.py
	fun=`basename $funtest .py`
	#### Mudando TAD celula
	cat $pythonfile $bindir/TAD_celula.py $funtest > $stoutdir/${fun}_celula.py
	#### Mudando TAD celula e coordenada
	cat $pythonfile $bindir/TAD_celula.py $bindir/TAD_coordenada.py $funtest > $stoutdir/${fun}_celula_coordenada.py
	#### Mudando TAD celula, coordenada e tabuleiro
	cat $pythonfile $bindir/TAD_celula.py $bindir/TAD_coordenada.py $bindir/TAD_tabuleiro.py $funtest > $stoutdir/${fun}_celula_coordenada_tab.py

	for py in $stoutdir/${fun}_*.py; do
	    echo "python3 $py"
	    python3 $py
	done

	## TESTES_hq
	funtest=$bindir/TESTES_hq.py
	fun=`basename $funtest .py`
	#### Mudando TAD celula, coordenada e tabuleiro
	cat $pythonfile $bindir/TAD_celula.py $bindir/TAD_coordenada.py $bindir/TAD_tabuleiro.py $funtest > $stoutdir/${fun}_celula_coordenada_tab.py
	#### Mudando TAD celula, coordenada, tabuleiro e portas
	cat $pythonfile $bindir/TAD_celula.py $bindir/TAD_coordenada.py $bindir/TAD_tabuleiro.py $bindir/TAD_portas.py $funtest > $stoutdir/${fun}_celula_coordenada_tab_portas.py

	for py in $stoutdir/${fun}_*.py; do
	    echo "python3 $py"
	    python3 $py
	done
}
##################################################

for student in `ls $indir`; do
  mkdir -p $outdir/$student/
  process_student $student | tee $outdir/$student/$student.log
done


# exit 0;
for d in $outdir/*; do
        N=`basename $d`;
        tab=`grep "TABULEIRO GLOBAL" $d/$N.log | cut -d'(' -f2 | cut -d' ' -f1 | awk '{acc+=$1}END{printf("%.2f\n",acc)}'`
        if [ -z "$tab" ]; then
                tab="0"
        fi
        por=`grep "PORTAS GLOBAL" $d/$N.log | cut -d'(' -f2 | cut -d' ' -f1 | awk '{acc+=$1}END{printf("%.2f\n",acc)}'`
        if [ -z "$por" ]; then
                por="0"
        fi
        hq=`grep "HELLO_QUANTUM GLOBAL" $d/$N.log | cut -d'(' -f2 | cut -d' ' -f1 | awk '{acc+=$1}END{printf("%.2f\n",acc)}'`
        if [ -z "$hq" ]; then
                hq="0"
        fi
        echo -e "$N\t$tab\t$por\t$hq"
done

exit 0;

for d in $outdir/*; do
	N=`basename $d`;
	STR="$N"
	# for teste in TESTES_*.py; do
		BLA=" GLOBAL"
		v=`grep "$BLA" $d/$N.log | cut -d'(' -f2 | cut -d' ' -f1`
		if [ -z "$v" ]; then
			v="0"
		fi
		N="$N\t$v"
	# done
	echo -e "$STR"
done

